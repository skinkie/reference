import aiohttp
import asyncio

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from vdv453 import StatusAnfrageType, StatusAntwortType, DatenBereitAnfrageType, DatenBereitAntwortType, AboAnfrageType, \
    AboAntwortType

BASE_URL = "http://127.0.0.1:8000/test"

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

async def get_status(session):
    status_anfrage_type = StatusAnfrageType(sender="test", zst=XmlDateTime.now())
    anfrage = serializer.render(status_anfrage_type)
    async with session.post(f"{BASE_URL}/aus/status.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
        print(resp.status)
        antwort = await resp.read()
        status_antwort_type = parser.from_bytes(antwort, StatusAntwortType)
        print(status_antwort_type)

async def get_daten_bereit(session):
    daten_bereit_anfrage_type = DatenBereitAnfrageType(sender="test", zst=XmlDateTime.now())
    anfrage = serializer.render(daten_bereit_anfrage_type)
    async with session.post(f"{BASE_URL}/aus/datenbereit.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
        print(resp.status)
        antwort = await resp.read()
        daten_bereit_antwort_type = parser.from_bytes(antwort, DatenBereitAntwortType)
        print(daten_bereit_antwort_type)

async def get_abo_anfrage(session):
    abo_anfrage_type = AboAnfrageType(sender="test", zst=XmlDateTime.now(), choice=[True])
    anfrage = serializer.render(abo_anfrage_type)
    async with session.post(f"{BASE_URL}/aus/aboverwalten.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
        print(resp.status)
        antwort = await resp.read()
        abo_antwort_type = parser.from_bytes(antwort, AboAntwortType)
        print(abo_antwort_type)

async def main():
    async with aiohttp.ClientSession() as session:
        # await get_status(session)
        # await get_daten_bereit(session)
        await get_abo_anfrage(session)

asyncio.run(main())