# This loop subscribes to the remote system, and assures that every hour a new subscription is made, a head of time.
import asyncio
import datetime
import aiohttp
from aiohttp import web
from xsdata.models.datatype import XmlDateTime

from storage import check_sender
from vdv453 import AboAnfrageType, AboAustype, AboAntwortType, DatenBereitAnfrageType, DatenBereitAntwortType, \
    BestaetigungType, ErgebnisType

from config import SENDER_ID
from generic import unknown_sender
from mqtt_communication import aus_datenabrufen

from xml_imports import parser, serializer

# Loop that assures that our remote subscription remains active
async def abo_anfrage(BASE_URL, TIMEOUT=3600):
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

async def aus_datenbereit(request):
    anfrage = await request.read()
    daten_bereit_anfrage_type = parser.from_bytes(anfrage, DatenBereitAnfrageType)
    if daten_bereit_anfrage_type.sender == request.match_info['sender']:
        uri = await check_sender(daten_bereit_anfrage_type.sender)
        if uri:
            antwort = DatenBereitAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.now()))
        else:
            antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))
    else:
        antwort = DatenBereitAntwortType(bestaetigung=unknown_sender(request))

    # Eigenlijk in de achtergrond draaien
    await asyncio.create_task(aus_datenabrufen(daten_bereit_anfrage_type.sender))
    await asyncio.sleep(0)

    return web.Response(text=serializer.render(antwort), content_type="application/xml")
