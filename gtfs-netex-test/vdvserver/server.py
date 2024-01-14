import asyncio

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
from vdv453 import DatenBereitAnfrageType, DatenBereitAntwortType, ErgebnisType, DatenAbrufenAnfrageType, \
    DatenAbrufenAntwortType, BestaetigungType, AboAnfrageType, AboAntwortType, AboAustype
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
                daten_bereit_anfrage_type = DatenBereitAnfrageType(sender=SENDER_ID, zst=XmlDateTime.now())
                anfrage = serializer.render(daten_bereit_anfrage_type)
                try:
                    url = f"{sender_uri[1]}/{SENDER_ID}/aus/datenbereit.xml"
                    logging.info(f"Notify {sender_uri[0]} via {url}.")
                    async with session.post(url, data=anfrage, headers={"Content-Type": "applicantion/xml"}) as resp:
                        print(resp.status)
                        antwort = await resp.read()
                        daten_bereit_antwort_type = parser.from_bytes(antwort, DatenBereitAntwortType)
                        print(daten_bereit_antwort_type)
                        if (daten_bereit_antwort_type.bestaetigung.ergebnis == ErgebnisType.NOTOK):
                            pass
                except:
                    pass

            await asyncio.sleep(60)

async def aus_datenabrufen(request):
    anfrage = await request.read()
    daten_abrufen_anfrage_type = parser.from_bytes(anfrage, DatenAbrufenAnfrageType)
    if daten_abrufen_anfrage_type.sender == request.match_info['sender']:
        uri = await check_sender(daten_abrufen_anfrage_type.sender)
        if uri is not None:
            antwort = DatenAbrufenAntwortType(bestaetigung=BestaetigungType(fehlernummer="0", zst=XmlDateTime.now(), ergebnis=ErgebnisType.OK), choice=await aus_nachrichten(sender=daten_abrufen_anfrage_type.sender))
        else:
            antwort = DatenAbrufenAntwortType(bestaetigung=unknown_sender(request))

    else:
        antwort = DatenAbrufenAntwortType(bestaetigung=unknown_sender(request))

    return web.Response(text=serializer.render(antwort), content_type="application/xml")

async def aus_aboverwalten(request):
    anfrage = await request.read()
    abo_anfrage_type = parser.from_bytes(anfrage, AboAnfrageType)
    if abo_anfrage_type.sender == request.match_info['sender']:
        uri = await check_sender(abo_anfrage_type.sender)
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
