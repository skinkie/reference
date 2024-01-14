import asyncio
import datetime
import aiomqtt
import gzip
import duckdb
import aiohttp
from aiohttp import web
from aiomqtt import ProtocolVersion
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties
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
SENDER_ID = "test"

db = duckdb.connect(DUCKDB_DATABASE)
mqtt_client = None

async def create_sender(BASE_URL, OUR_URI):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{BASE_URL}/anfrage", data=OUR_URI) as resp:
            print(resp.status)
            antwort = await resp.read()
            status_antwort_type = parser.from_bytes(antwort, StatusAntwortType)
            print(status_antwort_type)

async def checkSender(sender):
    """
    cursor = db.cursor()
    cursor.execute("SELECT uri FROM sender WHERE sender = ? LIMIT 1;", (sender,))
    results = cursor.fetchall()
    if len(results) >= 1:
        return results[0]

    return None
    """
    return sender in base_url

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

base_url = {}

async def aus_datenabrufen(SENDER):
    global mqtt_client
    BASE_URL = base_url.get(SENDER, None)
    if BASE_URL is None:
        return

    if mqtt_client is None:
        return

    async with aiohttp.ClientSession() as session:
        daten_afrufen_anfrage_type = DatenAbrufenAnfrageType(sender=SENDER_ID, zst=XmlDateTime.now())
        anfrage = serializer.render(daten_afrufen_anfrage_type)
        async with session.post(f"{BASE_URL}/aus/datenabrufen.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
            print(resp.status)
            antwort = await resp.read()
            daten_abrufen_antwort = parser.from_bytes(antwort, DatenAbrufenAntwortType)
            properties = Properties(PacketTypes.PUBLISH)
            properties.MessageExpiryInterval = 600  # in seconds

            # print(daten_abrufen_antwort)
            for aus_nachricht in daten_abrufen_antwort.choice:
                if isinstance(aus_nachricht, AusnachrichtType):
                    for istfahrt in aus_nachricht.choice:
                        if isinstance(istfahrt, IstFahrtType):
                            split_antwort = DatenAbrufenAntwortType(bestaetigung=daten_abrufen_antwort.bestaetigung, choice=[AusnachrichtType(abo_id=0, choice=[istfahrt])])
                            payload = serializer.render(split_antwort)
                            # print(payload)
                            payload = gzip.compress(bytes(payload, 'utf-8'))
                            await mqtt_client.publish(f"/VDV454/{SENDER}/{istfahrt.fahrt_ref.fahrt_id.betriebstag}/{istfahrt.linien_id}/{istfahrt.richtungs_id}/{istfahrt.fahrt_ref.fahrt_id.fahrt_bezeichner}", payload, retain=True, properties=properties)

@routes.post('/{sender}/aus/datenbereit.xml')
async def aus_datenbereit(request):
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

    await asyncio.create_task(aus_datenabrufen(daten_bereit_anfrage_type.sender))
    return web.Response(text=serializer.render(antwort), content_type="application/xml")

import logging
logging.basicConfig(filename='vdv453-client.log', level=logging.INFO)

app = web.Application()
app.add_routes(routes)

# This loop subscribes to the remote system, and assures that every hour a new subscription is made, a head of time.
async def get_abo_anfrage(BASE_URL, TIMEOUT=3600):
    async with aiohttp.ClientSession() as session:
        while True:
            verfall_zst = datetime.datetime.now() + datetime.timedelta(seconds=TIMEOUT)
            abo_anfrage_type = AboAnfrageType(sender=SENDER_ID, zst=XmlDateTime.now(), choice=[AboAustype(abo_id=1, verfall_zst=XmlDateTime.from_datetime(verfall_zst), hysterese=10, vorschauzeit=3600)])
            anfrage = serializer.render(abo_anfrage_type)
            async with session.post(f"{BASE_URL}/aus/aboverwalten.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                print(resp.status)
                antwort = await resp.read()
                abo_antwort_type = parser.from_bytes(antwort, AboAntwortType)
                print(abo_antwort_type)
            await asyncio.sleep(TIMEOUT - 60)

async def mqtt():
    async with aiomqtt.Client("192.168.5.32", username="stat", password="stat", protocol=ProtocolVersion.V5) as client:
        global mqtt_client
        mqtt_client = client
        while True:
            await asyncio.sleep(10)

async def main():
    global base_url
    base_url['NDOV'] = "http://192.168.5.32:8081/" + SENDER_ID
    await asyncio.gather(mqtt(), get_abo_anfrage(base_url['NDOV']), web._run_app(app, port=8082))

if __name__ == '__main__':
    # asyncio.run(create_sender("http://192.168.5.32:8081/test", "http://192.168.5.20:8082"))
    asyncio.run(main())
