from aiohttp import web
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from storage import check_daten_bereit
from vdv453 import StatusType, ErgebnisType, BestaetigungType, StatusAnfrage, \
    StatusAntwort

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.ignore_default_attributes = True
serializer_config.xml_declaration = True
serializer = XmlSerializer(serializer_config)

def unknown_sender(request) -> BestaetigungType:
    return BestaetigungType(fehlernummer="1", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.utcnow().replace(fractional_second=0),
                     fehlertext=f"I'm sorry, your sender {request.match_info['sender']} is not (yet) configured.")

async def aus_status(request):
    anfrage = await request.read()
    status_anfrage = parser.from_bytes(anfrage, StatusAnfrage)
    if status_anfrage.sender == request.match_info['sender']:
        daten_bereit = await check_daten_bereit(status_anfrage.sender)
        if daten_bereit is not None:
            antwort = StatusAntwort(status=StatusType(zst=XmlDateTime.utcnow().replace(fractional_second=0), ergebnis=ErgebnisType.OK), daten_bereit=daten_bereit,
                                        start_dienst_zst=XmlDateTime.utcnow().replace(fractional_second=0).replace(hour=4, minute=0, second=0))

        else:
            print("Sender not OK", status_anfrage.sender, request.match_info['sender'])
            antwort = StatusAntwort(status=StatusType(zst=XmlDateTime.utcnow().replace(fractional_second=0), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                                        start_dienst_zst=XmlDateTime.utcnow().replace(fractional_second=0).replace(hour=4, minute=0, second=0))
    else:
        print("Can't parse")
        antwort = StatusAntwort(status=StatusType(zst=XmlDateTime.utcnow().replace(fractional_second=0), ergebnis=ErgebnisType.NOTOK), daten_bereit=False,
                                    start_dienst_zst=XmlDateTime.utcnow().replace(fractional_second=0).replace(hour=4, minute=0, second=0))

    print(antwort)
    return web.Response(text=serializer.render(antwort), content_type="application/xml")
