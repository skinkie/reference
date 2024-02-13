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
    while True:
        try:
            async with aiomqtt.Client(MQTT_HOSTNAME, username=MQTT_USERNAME, password=MQTT_PASSWORD) as client:
                global mqtt_client
                mqtt_client = client

                async with client.messages() as messages:
                    await client.subscribe("/VDV454/stat/+/ARR/25060/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25672/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25061/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25062/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25063/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25064/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25065/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25066/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25073/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25074/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25076/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25078/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25079/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25080/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25081/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25083/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25084/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25085/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25422/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25411/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25415/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25412/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25413/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25414/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26019/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26639/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26632/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26041/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26047/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26048/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26655/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26659/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25087/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25088/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25370/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25371/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25372/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25377/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25421/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25441/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25442/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25443/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25444/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25601/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25602/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25674/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25675/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25679/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25789/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25790/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25792/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25794/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25796/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25798/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25799/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25811/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25812/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25813/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25089/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25683/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25684/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25687/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26015/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26633/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26637/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26640/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26647/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26043/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26046/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26201/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26202/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26203/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26204/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26205/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26206/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26207/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26208/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26209/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26259/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25067/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25068/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25069/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25289/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25662/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25663/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26001/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26002/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26003/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26004/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26005/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26006/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26007/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26008/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26009/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26010/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26027/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26028/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26030/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26031/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26032/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26033/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26034/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26036/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26037/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26038/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26039/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26040/#")
                    # await client.subscribe("/VDV454/stat/+/ARR/26044/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26051/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26052/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26053/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26054/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26055/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26056/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26057/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26059/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26350/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26631/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26652/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26657/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26723/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26791/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26793/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26795/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26797/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26803/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26016/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26017/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26018/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26616/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26012/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26603/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26606/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26617/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26618/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26643/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26650/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26658/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25686/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26011/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25161/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26635/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26831/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26013/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26035/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26210/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26321/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26322/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26332/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26431/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26432/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26433/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26434/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26601/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26615/#")
                    await client.subscribe("/VDV454/stat/+/ARR/26805/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25070/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25071/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25072/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25075/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25077/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25082/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25086/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25279/#")
                    await client.subscribe("/VDV454/stat/+/ARR/25298/#")

                    # await client.subscribe("/VDV454/stat/+/ARR/26044/#")
                    # await client.subscribe("/VDV454/stat/+/ARR/26350/#")
                    # await client.subscribe("/VDV454/stat/+/ARR/24189/#")
                    await client.subscribe("/VDV454/stat/+/+/S:18900/#")
                    await client.subscribe("/VDV454/stat/+/+/ST:18900/#")
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

        except:
            raise
        asyncio.sleep(15)

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
