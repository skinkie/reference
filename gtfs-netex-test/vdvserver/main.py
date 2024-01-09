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

def unknown_sender(request) -> BestaetigungType:
    return BestaetigungType(fehlernummer="1", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.now(),
                     fehlertext="I'm sorry, your {request.match_info['sender']} is not configured.")

@routes.post('/{sender}/aus/status.xml')
async def aus_status(request):
    anfrage = await request.read()
    status_anfrage_type = parser.from_bytes(anfrage, StatusAnfrageType)
    if status_anfrage_type.sender == request.match_info['sender']:
        antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK), daten_bereit=True,
                              start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))
    else:
        antwort = StatusAntwortType(status=StatusType(zst=XmlDateTime.now(), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                              start_dienst_zst=XmlDateTime.now().replace(hour=4, minute=0, second=0))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")

@routes.post('/{sender}/aus/datenbereit.xml')
async def aus_status(request):
    anfrage = await request.read()
    daten_bereit_anfrage_type = parser.from_bytes(anfrage, DatenBereitAnfrageType)
    if daten_bereit_anfrage_type.sender == request.match_info['sender']:
        antwort = DatenBereitAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))
    else:
        antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))

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

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)