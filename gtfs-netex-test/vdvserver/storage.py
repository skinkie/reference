import asyncio
import time
from typing import List

import aiohttp
import duckdb
import sqlite3
from xsdata.models.datatype import XmlDateTime

from vdv453 import AboAustype, DatenBereitAnfrageType, DatenBereitAntwortType, ErgebnisType, AusnachrichtType, \
    IstFahrtType

from config import SQLITE_DATABASE, DUCKDB_DATABASE, SENDER_ID, SERVER_SENDER_ID
from xml_imports import parser, serializer
import logging

# db = duckdb.connect(DUCKDB_DATABASE)
db = sqlite3.connect(SQLITE_DATABASE)

async def check_or_create_tables():
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sender (sender TEXT, epoch INTEGER, uri TEXT, PRIMARY KEY (sender));
                      CREATE TABLE IF NOT EXISTS abo (sender TEXT, abo_id INTEGER, linien_filter BOOLEAN, umlauf_filter BOOLEAN, hysterese INTEGER, vorschauzeit INTEGER, verfall_zst INTEGER, PRIMARY KEY (sender, abo_id), FOREIGN KEY(sender) REFERENCES sender (sender));
                      CREATE TABLE IF NOT EXISTS linien_filter (sender TEXT, abo_id INTEGER, linien_id TEXT, richtungs_id TEXT, PRIMARY KEY (sender, abo_id, linien_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));
                      CREATE TABLE IF NOT EXISTS umlauf_filter (sender TEXT, abo_id INTEGER, umlauf_id TEXT, PRIMARY KEY (sender, abo_id, umlauf_id), FOREIGN KEY(sender, abo_id) REFERENCES abo (sender, abo_id));
                      CREATE TABLE IF NOT EXISTS queue (journeyref TEXT, linien_id TEXT, richtungs_id TEXT, umlauf_id TEXT, expiry INTEGER, epoch INTEGER, message TEXT, PRIMARY KEY (journeyref));""")

async def create_sender(sender: str, uri: str):
    cursor = db.cursor()
    cursor.execute("INSERT OR REPLACE INTO sender VALUES (?, 0, ?);", (sender, uri,))

async def check_sender(sender: str) -> str:
    cursor = db.cursor()
    cursor.execute("SELECT uri FROM sender WHERE sender = ? LIMIT 1;", (sender,))
    results = cursor.fetchall()
    if len(results) >= 1:
        return results[0][0]

    return None

async def drop_sender(sender: str):
    cursor = db.cursor()
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM abo WHERE sender = ?;""", (sender,))

async def abo_loeschen_alle(sender: str):
    cursor = db.cursor()
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ?;""", (sender,))
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ? AND sender <> 'local' AND sender <> 'idsvrs01';""", (sender,))
    cursor.execute("""DELETE FROM abo WHERE sender = ?;""", (sender,))

async def abo_loeschen(sender: str, abo_id: int):
    cursor = db.cursor()
    cursor.execute("""DELETE FROM umlauf_filter WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))
    cursor.execute("""DELETE FROM linien_filter WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))
    cursor.execute("""DELETE FROM abo WHERE sender = ? AND abo_id = ?;""", (sender, abo_id,))

async def abo_aus(sender: str, abo_aus_type: AboAustype):
    await abo_loeschen(sender, abo_aus_type.abo_id)

    umlauf_filter = [(sender, abo_aus_type.abo_id, umlauf_id,) for umlauf_id in abo_aus_type.umlauf_id]
    linien_filter = [(sender, abo_aus_type.abo_id, linien_filter_type.linien_id, linien_filter_type.richtungs_id) for
                     linien_filter_type in abo_aus_type.linien_filter]

    cursor = db.cursor()
    cursor.executemany("INSERT INTO umlauf_filter (sender, abo_id, umlauf_id) VALUES (?, ?, ?);", umlauf_filter)
    cursor.executemany("INSERT INTO linien_filter (sender, abo_id, linien_id, richtungs_id) VALUES (?, ?, ?, ?);", linien_filter)
    cursor.execute("INSERT INTO abo (sender, abo_id, linien_filter, umlauf_filter, hysterese, vorschauzeit, verfall_zst) VALUES (?, ?, ?, ?, ?, ?, ?);",
                             (sender, abo_aus_type.abo_id, len(linien_filter) > 0, len(umlauf_filter) > 0, abo_aus_type.hysterese, abo_aus_type.vorschauzeit, int(abo_aus_type.verfall_zst.to_datetime().timestamp())))

async def queue_daten_bereit():
    cursor = db.cursor()
    async with aiohttp.ClientSession() as session:
        while True:
            cursor.execute("""select sender.sender, sender.uri from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) group by sender.sender, sender.uri having count(*) > 0;""")
            for sender_uri in cursor.fetchall():
                daten_bereit_anfrage_type = DatenBereitAnfrageType(sender=SERVER_SENDER_ID, zst=XmlDateTime.utcnow().replace(fractional_second=0))
                anfrage = serializer.render(daten_bereit_anfrage_type)
                try:
                    url = f"{sender_uri[1]}/{SERVER_SENDER_ID}/aus/datenbereit.xml"
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

            # TODO: terug naar 60
            await asyncio.sleep(60)

async def check_daten_bereit(sender: str):
    cursor = db.cursor()
    cursor.execute("""select count(*) from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender = ? AND sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id);""", (sender,))
    results = cursor.fetchall()
    if len(results) > 0:
        return results[0][0] > 0

    return None
async def queue_garbage_collector():
    cursor = db.cursor()
    while True:
        cursor.execute("""BEGIN TRANSACTION; DELETE FROM queue WHERE (expiry + 600) > epoch(now()::TIMESTAMP)::INTEGER; COMMIT;""")
        await asyncio.sleep(600)

async def aus_nachrichten(sender: str) -> List[AusnachrichtType]:
    epoch = int(time.time())
    results: List[AusnachrichtType] = []
    cursor = db.cursor()
    cursor.execute("""select abo.abo_id, message from sender JOIN abo USING (sender) LEFT JOIN linien_filter USING (abo_id) LEFT JOIN umlauf_filter USING (abo_id), queue where sender = ? and sender.epoch < queue.epoch and (linien_filter = false OR linien_filter.linien_id = queue.linien_id and (linien_filter.richtungs_id IS NULL OR linien_filter.richtungs_id = queue.richtungs_id)) and (umlauf_filter = false OR umlauf_filter.umlauf_id = queue.umlauf_id) order by abo_id;""", (sender,))
    for result in cursor.fetchall():
        abo_id, message = result
        try:
            ist_fahrt_type = parser.from_string(message, IstFahrtType)
        except:
            pass
        if len(results) == 0 or results[-1].abo_id != abo_id:
            results.append(AusnachrichtType(abo_id=abo_id, choice=[ist_fahrt_type]))
        else:
            results[-1].choice.append(ist_fahrt_type)

    cursor.execute("""UPDATE sender SET epoch = ? WHERE sender = ?""", (epoch, sender,))

    return results
