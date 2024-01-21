import gzip
from gzip import GzipFile
from io import BytesIO
import time

import aiohttp
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties
from xsdata.models.datatype import XmlDateTime

from storage import db, check_sender
from vdv453 import DatenAbrufenAntwortType, AusnachrichtType, IstFahrtType, DatenAbrufenAnfrageType

import aiomqtt

from config import SENDER_ID, MQTT_HOSTNAME, MQTT_PASSWORD, MQTT_USERNAME

from xml_imports import parser, serializer, serializer_db

mqtt_client = None
async def mqtt_subscriber():
    cursor = db.cursor()
    # i = 0
    async with aiomqtt.Client(MQTT_HOSTNAME, username=MQTT_USERNAME, password=MQTT_PASSWORD) as client:
        global mqtt_client
        mqtt_client = client

        async with client.messages() as messages:
            await client.subscribe("/VDV454/stat/#")
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

async def aus_datenabrufen(sender):
    print("In aus_datenabrufen")
    global mqtt_client
    url = await check_sender(sender)
    if url is None:
        return

    if mqtt_client is None:
        return

    async with aiohttp.ClientSession() as session:
        daten_afrufen_anfrage_type = DatenAbrufenAnfrageType(sender=SENDER_ID, zst=XmlDateTime.utcnow().replace(fractional_second=0), datensatz_alle=False)
        anfrage = serializer.render(daten_afrufen_anfrage_type)
        async with session.post(f"{url}/{SENDER_ID}/aus/datenabrufen.xml", data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
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
                            await mqtt_client.publish(f"/VDV454/{sender}/{istfahrt.fahrt_ref.fahrt_id.betriebstag}/{istfahrt.linien_id}/{istfahrt.richtungs_id}/{istfahrt.fahrt_ref.fahrt_id.fahrt_bezeichner}", payload, retain=True, properties=properties)
