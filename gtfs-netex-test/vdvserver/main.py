import asyncio
import logging
from typing import List, Tuple
import time
import duckdb
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
serializer_config.xml_declaration = True
serializer = XmlSerializer(serializer_config)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = False
serializer_config.ignore_default_attributes = True
serializer_config.xml_declaration = False
serializer_db = XmlSerializer(serializer_config)


DUCKDB_DATABASE = "vdv453.duckdb"
SENDER_ID = "NDOV"

db = duckdb.connect(DUCKDB_DATABASE)

async def checkOrCreateTables():
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sender (sender TEXT, epoch INTEGER, uri TEXT, PRIMARY KEY (sender));
                        CREATE TABLE IF NOT EXISTS abo (sender TEXT, abo_id INTEGER, linien_filter BOOLEAN, umlauf_filter BOOLEAN, hysterese INTEGER, vorschauzeit INTEGER, verfall_zst INTEGER, PRIMARY KEY (sender, abo_id), FOREIGN KEY(sender) REFERENCES sender (sender));
                        CREATE TABLE IF NOT EXISTS linien_filter (sender TEXT, abo_id INTEGER, linien_id TEXT, richtungs_id TEXT, PRIMARY KEY (sender, abo_id, linien_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));
                        CREATE TABLE IF NOT EXISTS umlauf_filter (sender TEXT, abo_id INTEGER, umlauf_id TEXT, PRIMARY KEY (sender, abo_id, umlauf_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));
                        CREATE TABLE IF NOT EXISTS queue (journeyref TEXT, linien_id TEXT, richtungs_id TEXT, umlauf_id TEXT, expiry INTEGER, epoch INTEGER, message TEXT, PRIMARY KEY (journeyref));""")

async def dropSender(sender: str):
    cursor = db.cursor()
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM abo WHERE sender = ?;""", (sender,))

async def checkSender(sender):
    cursor = db.cursor()
    cursor.execute("SELECT uri FROM sender WHERE sender = ? LIMIT 1;", (sender,))
    results = cursor.fetchall()
    if len(results) >= 1:
        return results[0]

    return None

async def checkDataAvailable(epoch):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM messages WHERE epoch < ?;", (epoch,))
    results = cursor.fetchall()
    if results[0][0] > 0:
        return True

# Should be sent with every incoming update matching the subscription.
async def sendDatenBereit(sender):
    cursor = db.cursor()
    cursor.execute("SELECT sender, uri FROM abo WHERE sender = ?;", (sender,))
    async with aiohttp.ClientSession() as session:
        for result in cursor.fetchone():
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

from urllib.parse import urlparse
import socket
@routes.post('/{sender}/anfrage')
async def sender_create(request):
    uri = await request.read()
    try:
        result = urlparse(uri)
        if request.remote == socket.gethostbyname(result.netloc.decode('utf-8').split(':')[0]):
            cursor = db.cursor()
            cursor.execute("INSERT OR REPLACE INTO sender VALUES (?, 0, ?);", (request.match_info['sender'], uri))

            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK), daten_bereit=True,
                                        start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))
            return web.Response(text=serializer.render(antwort), content_type="application/xml")
    except:
        raise

    antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                                start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))
    return web.Response(text=serializer.render(antwort), content_type="application/xml")

@routes.post('/{sender}/aus/status.xml')
async def aus_status(request):
    anfrage = await request.read()
    status_anfrage_type = parser.from_bytes(anfrage, StatusAnfrageType)
    if status_anfrage_type.sender == request.match_info['sender']:
        uri = await checkSender(status_anfrage_type.sender)
        if uri is not None:
            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK), daten_bereit=True,
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
    epoch = int(time.time())
    results: List[AusnachrichtType] = []
    cursor = db.cursor()
    cursor.execute("""select abo.abo_id, message from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender = ? and sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) order by abo_id;""", (sender,))
    for result in cursor.fetchall():
        abo_id, message = result
        ist_fahrt_type = parser.from_bytes(message, IstFahrtType)
        if len(results) == 0 or results[-1].abo_id != abo_id:
            results.append(AusnachrichtType(abo_id=abo_id, choice=[ist_fahrt_type]))
        else:
            results[-1].choice.append(ist_fahrt_type)

    cursor.execute("""UPDATE sender SET epoch = ? WHERE sender = ?""", (epoch, sender,))

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
    cursor = db.cursor()
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM abo WHERE sender = ?;""", (sender,))

async def abo_loeschen(sender: str, abo_id: int):
    cursor = db.cursor()
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))
    cursor.execute("""DELETE FROM abo WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))

async def abo_aus(sender: str, abo_aus_type: AboAustype):
    umlauf_filter = [(sender, abo_aus_type.abo_id, umlauf_id,) for umlauf_id in abo_aus_type.umlauf_id]
    linien_filter = [(sender, abo_aus_type.abo_id, linien_filter_type.linien_id, linien_filter_type.richtungs_id) for
                     linien_filter_type in abo_aus_type.linien_filter]

    cursor = db.cursor()
    cursor.executemany("INSERT INTO umlauf_filter (sender, abo_id, umlauf_id) VALUES (?, ?, ?);", umlauf_filter)
    cursor.executemany("INSERT INTO linien_filter (sender, abo_id, linien_id, richtungs_id) VALUES (?, ?, ?, ?);", linien_filter)
    cursor.execute("INSERT INTO abo (sender, abo_id, linien_filter, umlauf_filter, hysterese, vorschauzeit, verfall_zst) VALUES (?, ?, ?, ?, ?, ?, ?);",
                             (sender, abo_aus_type.abo_id, len(linien_filter) > 0, len(umlauf_filter) > 0, abo_aus_type.hysterese, abo_aus_type.vorschauzeit, int(abo_aus_type.verfall_zst.to_datetime().timestamp())))
    await abo_loeschen(sender, abo_aus_type.abo_id)

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


import aiomqtt
from gzip import GzipFile
from io import BytesIO

async def mqtt_subscriber():
    cursor = db.cursor()
    # i = 0
    async with aiomqtt.Client("127.0.0.1", username="stat", password="stat") as client:
        async with client.messages() as messages:
            await client.subscribe("/VDV454/#")
            async for message in messages:
                daten_abrufen_antwort = None
                try:
                    content = GzipFile('','r',0,BytesIO(message.payload)).read()
                    daten_abrufen_antwort = parser.from_bytes(content, DatenAbrufenAntwortType)
                except:
                    pass

                if daten_abrufen_antwort is not None and isinstance(daten_abrufen_antwort.choice, list):
                    l = []
                    for aus_nachricht in daten_abrufen_antwort.choice:
                        if isinstance(aus_nachricht, AusnachrichtType):
                            for istfahrt in aus_nachricht.choice:
                                if isinstance(istfahrt, IstFahrtType):
                                    l.append((istfahrt.fahrt_ref.fahrt_id.fahrt_bezeichner, istfahrt.linien_id, istfahrt.richtungs_id, istfahrt.umlauf_id, istfahrt.fahrt_ref.fahrt_start_ende[0].endzeit.to_datetime().timestamp(), int(time.time()), serializer_db.render(istfahrt),))

                    if len(l) > 0:
                        cursor.executemany("""INSERT OR REPLACE INTO queue VALUES (?, ?, ?, ?, ?, ?, ?);""", l)
                        # cursor.close()

                    # i += 1
                    # if i == 100000:
                    #    raise Exception('Stop this thing')

                # print(message.payload)

async def queue_garbage_collector():
    cursor = db.cursor()
    while True:

        cursor.execute("""BEGIN TRANSACTION; DELETE FROM queue WHERE (expiry + 600) > epoch(now()::TIMESTAMP)::INTEGER; COMMIT;""")
        await asyncio.sleep(600)

    cursor.close()

import logging
logging.basicConfig(filename='vdv453.log', level=logging.INFO)

async def queue_daten_bereit():
    cursor = db.cursor()
    async with aiohttp.ClientSession() as session:
        while True:
            cursor.execute("""select sender.sender, sender.uri from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) group by sender.sender, sender.uri having count(*) > 0;""")
            for sender_uri in cursor.fetchall():
                daten_bereit_anfrage_type = DatenBereitAnfrageType(sender=SENDER_ID, zst=XmlDateTime.now())
                anfrage = serializer.render(daten_bereit_anfrage_type)
                try:
                    logging.info(f"Notify {sender_uri[0]} via {sender_uri[1]}.")
                    async with session.post(f"{sender_uri[1]}/aus/datenbereit.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                        print(resp.status)
                        antwort = await resp.read()
                        daten_bereit_antwort_type = parser.from_bytes(antwort, DatenBereitAntwortType)
                        print(daten_bereit_antwort_type)
                except:
                    pass

            await asyncio.sleep(60)
    cursor.close()

app = web.Application()
app.add_routes(routes)

async def main():
    await asyncio.gather(mqtt_subscriber(), web._run_app(app, port=8081), queue_garbage_collector(), queue_daten_bereit())

if __name__ == '__main__':
    asyncio.run(checkOrCreateTables())
    asyncio.run(main())
