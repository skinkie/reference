import asyncio
import gzip

import aiohttp
from aiohttp import web
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from generic import unknown_sender
from storage import db, check_sender, abo_loeschen_alle, abo_loeschen, abo_aus, aus_nachrichten
from vdv453 import ErgebnisType, \
    BestaetigungType, AboAustype, DatenAbrufenAntwort, \
    AboAnfrage, AboAntwort, DatenBereitAnfrage, DatenBereitAntwort, DatenAbrufenAnfrage
from config import SENDER_ID

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.ignore_default_attributes = True
serializer_config.xml_declaration = True
serializer = XmlSerializer(serializer_config)

import logging

async def queue_daten_bereit():
    cursor = db.cursor()
    async with aiohttp.ClientSession() as session:
        while True:
            cursor.execute("""select sender.sender, sender.uri from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) group by sender.sender, sender.uri having count(*) > 0;""")
            for sender_uri in cursor.fetchall():
                daten_bereit_anfrage = DatenBereitAnfrage(sender=SENDER_ID, zst=XmlDateTime.utcnow().replace(fractional_second=0))
                anfrage = serializer.render(daten_bereit_anfrage)
                try:
                    url = f"{sender_uri[1]}/{SENDER_ID}/aus/datenbereit.xml"
                    logging.info(f"Notify {sender_uri[0]} via {url}.")
                    async with session.post(url, data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                        print(resp.status)
                        antwort = await resp.read()
                        daten_bereit_antwort = parser.from_bytes(antwort, DatenBereitAntwort)
                        print(daten_bereit_antwort)
                        if (daten_bereit_antwort.bestaetigung.ergebnis == ErgebnisType.NOTOK):
                            pass
                except:
                    pass

            await asyncio.sleep(15)

async def aus_datenabrufen(request):
    anfrage = await request.read()
    daten_abrufen_anfrage = parser.from_bytes(anfrage, DatenAbrufenAnfrage)
    if daten_abrufen_anfrage.sender == request.match_info['sender']:
        uri = await check_sender(daten_abrufen_anfrage.sender)
        if uri is not None:
            antwort = DatenAbrufenAntwort(bestaetigung=BestaetigungType(fehlernummer="0", zst=XmlDateTime.utcnow().replace(fractional_second=0), ergebnis=ErgebnisType.OK), choice=await aus_nachrichten(sender=daten_abrufen_anfrage.sender))
        else:
            antwort = DatenAbrufenAntwort(bestaetigung=unknown_sender(request))

    else:
        antwort = DatenAbrufenAntwort(bestaetigung=unknown_sender(request))

    #return web.Response(body=gzip.compress(bytes(serializer.render(antwort), 'utf-8')), headers={"Content-Encoding": "gzip"}, content_type="application/xml")
    return web.Response(text=serializer.render(antwort), content_type="application/xml")

async def aus_aboverwalten(request):
    anfrage = await request.read()
    abo_anfrage = parser.from_bytes(anfrage, AboAnfrage)
    if abo_anfrage.sender == request.match_info['sender']:
        uri = await check_sender(abo_anfrage.sender)
        if uri:
            if isinstance(abo_anfrage.choice, bool):
                await abo_loeschen_alle(abo_anfrage.sender)
                antwort = AboAntwort(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.utcnow().replace(fractional_second=0)))

            elif isinstance(abo_anfrage.choice, int):
                await abo_loeschen(abo_anfrage.sender, abo_anfrage.choice)
                antwort = AboAntwort(bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.OK, zst=XmlDateTime.utcnow().replace(fractional_second=0)))

            elif isinstance(abo_anfrage.choice, list):
                abo_aus_types = [abo_aus_type for abo_aus_type in abo_anfrage.choice if isinstance(abo_aus_type, AboAustype)]
                for abo_aus_type in abo_aus_types:
                    await abo_aus(abo_anfrage.sender, abo_aus_type)

                ids = ', '.join([str(abo_aus_type.abo_id) for abo_aus_type in abo_aus_types])
                antwort = AboAntwort(bestaetigung=BestaetigungType(fehlernummer="0", fehlertext=f"Adding/Replacing abo_id(s) {ids} for {abo_anfrage.sender}.", ergebnis=ErgebnisType.OK, zst=XmlDateTime.utcnow().replace(fractional_second=0)))

            else:
                antwort = AboAntwort(
                    bestaetigung=BestaetigungType(fehlernummer="0", ergebnis=ErgebnisType.NOTOK, zst=XmlDateTime.utcnow().replace(fractional_second=0), fehlertext="This operation is not implemented."))
        else:
            antwort = AboAntwort(bestaetigung=unknown_sender(request))

    else:
        antwort = AboAntwort(bestaetigung=unknown_sender(request))

    print(anfrage.decode('utf-8'))
    text = serializer.render(antwort)
    print(text)

    return web.Response(text=text, content_type="application/xml")
