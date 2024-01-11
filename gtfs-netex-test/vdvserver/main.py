import asyncio
from typing import List, Tuple
import time
import aioduckdb
import aiohttp
from aiohttp import web
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDate

from vdv453 import StatusAnfrageType, StatusAntwortType, StatusType, ErgebnisType, DatenBereitAnfrageType, \
    DatenBereitAntwortType, BestaetigungType, AboAnfrageType, AboAntwortType, AboAustype, DatenAbrufenAnfrageType, \
    DatenAbrufenAntwortType, AusnachrichtType, IstFahrtType, FahrtRefType, FahrtIdtype

routes = web.RouteTableDef()

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

DUCKDB_DATABASE = "vdv453.duckdb"

async def checkOrCreateTables():
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS sender (sender TEXT, epoch INTEGER, uri TEXT, PRIMARY KEY (sender));")
        await db.execute("CREATE TABLE IF NOT EXISTS abo (sender TEXT, abo_id INTEGER, linien_filter BOOLEAN, umlauf_filter BOOLEAN, hysterese INTEGER, vorschauzeit INTEGER, verfall_zst INTEGER, PRIMARY KEY (sender, abo_id), FOREIGN KEY(sender) REFERENCES sender (sender));")
        await db.execute("CREATE TABLE IF NOT EXISTS linien_filter (sender TEXT, abo_id INTEGER, linien_id TEXT, richtungs_id TEXT, PRIMARY KEY (sender, abo_id, linien_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));")
        await db.execute("CREATE TABLE IF NOT EXISTS umlauf_filter (sender TEXT, abo_id INTEGER, umlauf_id TEXT, PRIMARY KEY (sender, abo_id, umlauf_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));")
        await db.execute("CREATE TABLE IF NOT EXISTS queue (journeyref TEXT, linien_id TEXT, richtungs_id TEXT, umlauf_id TEXT, expiry INTEGER, epoch INTEGER, message TEXT, PRIMARY KEY (journeyref));")

async def dropSender(sender: str):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        await db.execute("DELETE FROM linien_filter WHERE sender = ?;")
        await db.execute("DELETE FROM umlauf_filter WHERE sender = ?;")
        await db.execute("DELETE FROM abo WHERE sender = ?;")
        await db.execute("DELETE FROM sender WHERE sender = ?;")


"""
async def checkSender(sender):
    db = await aioduckdb.connect(DUCKDB_DATABASE)
    cursor = await db.execute("SELECT uri FROM sender WHERE sender = ? LIMIT 1;", (sender,))
    results = await cursor.fetchall()
    if len(results) >= 1:
        return results[0]

    return None
"""

async def checkSender(sender):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT uri FROM sender WHERE sender = ? LIMIT 1;", (sender,)) as cursor:
            results = await cursor.fetchall()
            if len(results) >= 1:
                return results[0]

    return None


async def checkDataAvailable(epoch):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT COUNT(*) FROM messages WHERE epoch < ?;", (epoch,)) as cursor:
            results = cursor.fetchall()
            if results[0][0] > 0:
                return True

# Should be sent with every incoming update matching the subscription.
async def sendDatenBereit():
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT sender, uri FROM subscription;") as cursor:
            async with aiohttp.ClientSession() as session:
                async for result in cursor:
                    sender, epoch, uri = result
                    daten_bereit_anfrage_type = DatenBereitAnfrageType(sender=sender, zst=XmlDateTime.now())
                    anfrage = serializer.render(daten_bereit_anfrage_type)
                    async with session.post(f"{uri}/aus/datenbereit.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                        antwort = await resp.read()
                        daten_bereit_antwort_type = parser.from_bytes(antwort, DatenBereitAntwortType)
                        print(daten_bereit_antwort_type)


def unknown_sender(request) -> BestaetigungType:
    return BestaetigungType(fehlernummer="1", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.now(),
                     fehlertext=f"I'm sorry, your sender {request.match_info['sender']} is not (yet) configured.")

@routes.post('/{sender}/aus/status.xml')
async def aus_status(request):
    anfrage = await request.read()
    status_anfrage_type = parser.from_bytes(anfrage, StatusAnfrageType)
    if status_anfrage_type.sender == request.match_info['sender']:
        uri = await checkSender(status_anfrage_type.sender)
        if uri is not None:
            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK),
                                        start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))

        else:
            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK),
                                        daten_bereit=False,
                                        start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))
    else:
        antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                              start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")

async def aus_nachrichten(sender: str) -> List[AusnachrichtType]:
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        """
        epoch: int = 0
        async with db.execute("SELECT epoch FROM sender WHERE sender = ? LIMIT 1;", (sender,)) as cursor:
            results = await cursor.fetchall()
            if len(results) >= 1:
                epoch = results[0]

        abos = {}

        async with db.execute("SELECT abo_id, hysterese, vorschauzeit FROM abo WHERE sender = ?;", (sender,)) as cursor:
            async for result in cursor:
                abo_id, line_filter, umlauf_filter, hysterese, vorschauzeit = result
                abos[abo_id] = {'abo_id': abo_id, 'hysterese': hysterese, 'vorschauzeit': vorschauzeit, 'linien_filter': [], 'umlauf_filter': []}

        async with db.execute("SELECT abo_id, linien_id, richtungs_id FROM linien_filter WHERE sender = ?;", (sender,)) as cursor:
            async for result in cursor:
                abo_id, linien_id, richtungs_id = result
                abos[abo_id]['linien_filter'].append({'linien_id': linien_id, 'richtungs_id': richtungs_id})

        async with db.execute("SELECT abo_id, umlauf_id FROM umlauf_filter WHERE sender = ?;", (sender,)) as cursor:
            async for result in cursor:
                abo_id, umlauf_id = result
                abos[abo_id]['umlauf_filter'].append({'umlauf_id': umlauf_id})

        unfiltered = len([abo for abo in abos.values() if len(abo['linien_filter']) == 0 and len(abo['umlauf_filter']) == 0]) > 0
        """

        """
        if unfiltered:
            async with db.execute("SELECT message FROM queue WHERE epoch > ?;", (epoch,)) as cursor:
                async for result in cursor:
                    pass
        else:
            SELECT abo_id, message FROM sender, queue, abo, linien_filter WHERE
            sender.sender = ? AND sender.epoch > queue.epoch AND
            sender.sender = abo.sender AND
            (line_filter.linien_id IS NULL OR line_filter.linien_id = queue.linien_id) AND
            (line_filter.richtungs_id IS NULL OR line_filter.richtungs_id = queue.richtungs_id)
        """

        epoch = int(time.time())
        results: List[AusnachrichtType] = []
        async with db.execute("""select abo.abo_id, message from sender JOIN abo USING (sender) LEFT jOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender = ? and sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) order by abo_id;""", (sender,)) as cursor:
            async for result in cursor:
                abo_id, message = result
                ist_fahrt_type: IstFahrtType = IstFahrtType(fahrt_ref=FahrtRefType(fahrt_id=FahrtIdtype(fahrt_bezeichner="1", betriebstag=XmlDate.today())), linien_id="1", richtungs_id="1", komplettfahrt=True) # parser.from_bytes(message, IstFahrtType)
                if len(results) == 0 or results[-1].abo_id != abo_id:
                    results.append(AusnachrichtType(abo_id=abo_id, choice=[ist_fahrt_type]))
                else:
                    results[-1].choice.append(ist_fahrt_type)

        await db.execute("""update sender set epoch = ? where sender = ?""", (epoch, sender,))

        return results

@routes.post('/{sender}/aus/datenabrufen.xml')
async def aus_datenabrufen(request):
    anfrage = await request.read()
    daten_abrufen_anfrage_type = parser.from_bytes(anfrage, DatenAbrufenAnfrageType)
    if daten_abrufen_anfrage_type.sender == request.match_info['sender']:
        uri = await checkSender(daten_abrufen_anfrage_type.sender)
        if uri is not None:
            antwort = DatenAbrufenAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK), choice=await aus_nachrichten(sender=daten_abrufen_anfrage_type.sender))
        else:
            antwort = DatenAbrufenAntwortType(bestaetigung=unknown_sender(request))

    else:
        antwort = DatenAbrufenAntwortType(bestaetigung=unknown_sender(request))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")

async def abo_loeschen_alle(sender: str):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        await db.execute("DELETE FROM umlauf_filter WHERE sender = ?", (sender,))
        await db.execute("DELETE FROM linien_filter WHERE sender = ?", (sender,))
        await db.execute("DELETE FROM abo WHERE sender = ?;", (sender,))

async def abo_loeschen(sender: str, abo_id: int):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        await db.execute("DELETE FROM umlauf_filter WHERE sender = ? AND abo_id = ?", (sender, abo_id,))
        await db.execute("DELETE FROM linien_filter WHERE sender = ? AND abo_id = ?", (sender, abo_id,))
        await db.execute("DELETE FROM abo WHERE sender = ? AND abo_id = ?;", (sender, abo_id,))

async def abo_aus(sender: str, abo_aus_type: AboAustype):
    umlauf_filter = [(sender, abo_aus_type.abo_id, umlauf_id,) for umlauf_id in abo_aus_type.umlauf_id]
    linien_filter = [(sender, abo_aus_type.abo_id, linien_filter_type.linien_id, linien_filter_type.richtungs_id) for
                     linien_filter_type in abo_aus_type.linien_filter]

    await abo_loeschen(sender, abo_aus_type.abo_id)
    async with (aioduckdb.connect(DUCKDB_DATABASE) as db):
        await db.executemany("INSERT INTO umlauf_filter (sender, abo_id, umlauf_id) VALUES (?, ?, ?);", umlauf_filter)
        await db.executemany("INSERT INTO linien_filter (sender, abo_id, linien_id, richtungs_id) VALUES (?, ?, ?, ?);", linien_filter)
        await db.execute("INSERT INTO abo (sender, abo_id, epoch, linien_filter, umlauf_filter, hysterese, vorschauzeit, verfall_zst) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                             (sender, abo_aus_type.abo_id, 0, len(linien_filter) > 0, len(umlauf_filter) > 0, abo_aus_type.hysterese, abo_aus_type.vorschauzeit, int(abo_aus_type.verfall_zst.to_datetime().timestamp())))

@routes.post('/{sender}/aus/aboverwalten.xml')
async def aus_aboverwalten(request):
    anfrage = await request.read()
    abo_anfrage_type = parser.from_bytes(anfrage, AboAnfrageType)
    if abo_anfrage_type.sender == request.match_info['sender']:
        uri = await checkSender(abo_anfrage_type.sender)
        if uri:
            if isinstance(abo_anfrage_type.choice, bool):
                await abo_loeschen_alle(abo_anfrage_type.sender)
                antwort = AboAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))

            elif isinstance(abo_anfrage_type.choice, int):
                await abo_loeschen(abo_anfrage_type.sender, abo_anfrage_type.choice)
                antwort = AboAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))

            elif isinstance(abo_anfrage_type.choice, list):
                abo_aus_types = [abo_aus_type for abo_aus_type in abo_anfrage_type.choice if isinstance(abo_aus_type, AboAustype)]
                for abo_aus_type in abo_aus_types:
                    await abo_aus(abo_anfrage_type.sender, abo_aus_type)

                ids = ', '.join([str(abo_aus_type.abo_id) for abo_aus_type in abo_aus_types])
                antwort = AboAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", fehlertext=f"Adding/Replacing abo_id(s) {ids} for {abo_anfrage_type.sender}.", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))

            else:
                antwort = AboAntwortType(
                    bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.now(), fehlertext="This operation is not implemented."))
        else:
            antwort = AboAntwortType(bestaetigung=unknown_sender(request))

    else:
        antwort = AboAntwortType(bestaetigung=unknown_sender(request))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")


# Code for a consuming application
@routes.post('/{sender}/aus/datenbereit.xml')
async def aus_status(request):
    anfrage = await request.read()
    daten_bereit_anfrage_type = parser.from_bytes(anfrage, DatenBereitAnfrageType)
    if daten_bereit_anfrage_type.sender == request.match_info['sender']:
        uri = await checkSender(daten_bereit_anfrage_type.sender)
        if uri:
            antwort = DatenBereitAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))
        else:
            antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))
    else:
        antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    # asyncio.run(checkOrCreateTables())
    web.run_app(app)