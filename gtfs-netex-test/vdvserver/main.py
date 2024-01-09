import aioduckdb
import aiohttp
from aiohttp import web
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from vdv453 import StatusAnfrageType, StatusAntwortType, StatusType, ErgebnisType, DatenBereitAnfrageType, \
    DatenBereitAntwortType, BestaetigungType, AboAnfrageType, AboAntwortType, AboAustype

routes = web.RouteTableDef()

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

DUCKDB_DATABASE = "vdv453.duckdb"

async def checkSubscription(sender):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT epoch, uri FROM subscription WHERE sender = ? LIMIT 1;", (sender,)) as cursor:
            results = cursor.fetchall()
            if len(results) > 1:
                return results[0], results[1]

    return None, None


async def checkDataAvailable(epoch):
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT COUNT(*) FROM messages WHERE epoch < ?;", (epoch,)) as cursor:
            results = cursor.fetchall()
            if results[0][0] > 0:
                return True

# Should be sent with every incoming update matching the subscription.
async def sendDataAvailable():
    async with aioduckdb.connect(DUCKDB_DATABASE) as db:
        async with db.execute("SELECT sender, uri FROM subscription;") as cursor:
            async with aiohttp.ClientSession() as session:
                for result in cursor:
                    sender, epoch, uri = result
                    daten_bereit_anfrage_type = DatenBereitAnfrageType(sender=sender, zst=XmlDateTime.now())
                    anfrage = serializer.render(daten_bereit_anfrage_type)
                    async with session.post(f"{uri}/aus/datenbereit.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                        antwort = await resp.read()
                        daten_bereit_antwort_type = parser.from_bytes(antwort, DatenBereitAntwortType)
                        print(daten_bereit_antwort_type)


def unknown_sender(request) -> BestaetigungType:
    return BestaetigungType(fehlernummer="1", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.now(),
                     fehlertext=f"I'm sorry, your subscription {request.match_info['sender']} is not (yet) configured.")

@routes.post('/{sender}/aus/status.xml')
async def aus_status(request):
    anfrage = await request.read()
    status_anfrage_type = parser.from_bytes(anfrage, StatusAnfrageType)
    if status_anfrage_type.sender == request.match_info['sender']:
        epoch, uri = await checkSubscription(status_anfrage_type.sender)
        if epoch is not None:
            daten_bereit = await checkDataAvailable(epoch)
            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK),
                                        daten_bereit=daten_bereit, start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))

        else:
            antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK),
                                        daten_bereit=False,
                                        start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))
    else:
        antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                              start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")


@routes.post('/{sender}/aus/datenabrufen.xml')
async def aus_datenabrufen(request):
     return web.Response(text="Hello, {}".format(request.match_info['sender']), content_type="application/xml")


@routes.post('/{sender}/aus/aboverwalten.xml')
async def aus_aboverwalten(request):
    anfrage = await request.read()
    abo_anfrage_type = parser.from_bytes(anfrage, AboAnfrageType)
    if abo_anfrage_type.sender == request.match_info['sender']:
        if isinstance(abo_anfrage_type.choice, bool):
            # AboLoeschenAlle
            pass
        elif isinstance(abo_anfrage_type.choice, int):
            # AboLoeschen
            pass
        elif isinstance(abo_anfrage_type.choice, AboAustype):
            # AboAUS
            pass
        else:
            pass
        print(abo_anfrage_type.choice)
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
        # Schedule a new fetch
        epoch, uri = await checkSubscription(daten_bereit_anfrage_type.sender)
        daten_bereit = False
        if epoch is not None:
            daten_bereit = await checkDataAvailable(epoch)

        antwort = DatenBereitAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))
    else:
        antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)