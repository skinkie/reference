import functools
import pickle
import queue
import threading
from typing import Generator

from netexio.database import Database
from netexio.dbaccess import update_embedded_referencing
from netexio.serializer import Serializer
from utils import get_object_name

def embedding_update(db: Database):
    task_queue = queue.Queue(maxsize=1000)  # Prevents excessive memory usage
    stop_signal = object()  # Special object to signal the writer to stop
    db_embedding = db.lmdb.open_db(b"_embedding")
    db_referencing = db.lmdb.open_db(b"_referencing")

    # Drop existing databases
    with db.lmdb.begin(write=True) as txn:
        txn.drop(db_embedding, delete=False)
        txn.drop(db_referencing, delete=False)

    def reader(table):
        """ Reads from the table and pushes modified data to the queue. """
        with db.lmdb.begin(write=False, db=db.open_table(table)) as txn_ro:
            cursor = txn_ro.cursor()
            for db_key, db_value in cursor:  # Rename outer loop variables
                i, j = 0, 0
                deserialized = db.serializer.unmarshall(db_value, table)

                for embedding in update_embedded_referencing(db.serializer, deserialized):
                    key_data = (embedding[0], embedding[1], embedding[2])
                    if embedding[7] is None:
                        embedding_key = (*key_data, i)
                        embedding_value = (embedding[3], embedding[4], embedding[5], embedding[6], embedding[7])
                        task_queue.put((b"_embedding", embedding_key, embedding_value))
                        i += 1
                    else:
                        ref_key = (*key_data, j)
                        ref_value = (embedding[3], embedding[4], embedding[5], embedding[6])
                        task_queue.put((b"_referencing", ref_key, ref_value))
                        j += 1

    def writer():
        """ Continuously writes data from the queue to LMDB in batches. """
        while True:
            batch = []
            try:
                # Fetch up to 100 items from the queue
                for _ in range(100):
                    batch.append(task_queue.get(timeout=3))
            except queue.Empty:
                if not batch:
                    break  # Stop if queue remains empty

            # Use a short-lived transaction for each batch
            with db.lmdb.begin(write=True) as txn:
                for db_name, key, value in batch:
                    if db_name == stop_signal:  # Stop signal received
                        return  # Exit writer function

                    db_handle = db_embedding if db_name == b"_embedding" else db_referencing
                    txn.put(pickle.dumps(key), pickle.dumps(value), db=db_handle)

    # Start writer thread
    writer_thread = threading.Thread(target=writer, daemon=True)
    writer_thread.start()

    # Spawn reader threads
    reader_threads = []
    for table in db.tables():
        thread = threading.Thread(target=reader, args=(table,))
        thread.start()
        reader_threads.append(thread)

    # Wait for all readers to finish
    for thread in reader_threads:
        thread.join()

    # Signal the writer to stop and wait for it to finish
    task_queue.put((stop_signal, None, None))
    writer_thread.join()

"""
def embedding_udf(serializer: Serializer, serialized: bytes, clazz: str) -> list[str]:
    deserialized = serializer.unmarshall(serialized, clazz)
    return [x for x in update_embedded_referencing(serializer, deserialized) if len(x) > 0]
    # return result

def embedding_update(db: Database):
    # We could likely optimise this a bit if we can do something smart with filtering
    with db.lmdb.begin(write=True) as txn:
        txn.drop(db.lmdb.open_db("_embedding".encode('utf-8')), delete=False)
        txn.drop(db.lmdb.open_db("_referencing".encode('utf-8')), delete=False)

    with db.lmdb.begin(write=True, db=db.lmdb.open_db("_embedding".encode('utf-8'))) as txn1:
        with db.lmdb.begin(write=True, db=db.lmdb.open_db("_referencing".encode('utf-8'))) as txn2:
            for table in db.tables():
                with db.lmdb.begin(write=False, db=db.open_table(table)) as txn_ro:
                    cursor = txn.cursor()
                    for key, value in cursor:
                        i = 0
                        j = 0
                        deserialized = db.serializer.unmarshall(value)
                        for embedding in update_embedded_referencing(db.serializer, deserialized):

                            if embedding[7] is None:
                                key = (embedding[0], embedding[1], embedding[2], i)
                                value = (embedding[3], embedding[4], embedding[5], embedding[6], embedding[7])
                                txn1.put(pickle.dumps(key), pickle.dumps(value))
                                i += 1
                            else:
                                key = (embedding[0], embedding[1], embedding[2], j)
                                value = (embedding[3], embedding[4], embedding[5], embedding[6])
                                txn2.put(pickle.dumps(key), pickle.dumps(value))
                                j += 1
"""



def embedding_update_duckdb(db: Database, clean=False, filter_clazz=None):
    con = db.con
    con.create_function('embedding', functools.partial(embedding_udf, db.serializer), return_type=list[str])

    sql_create_table = "CREATE TEMPORARY TABLE IF NOT EXISTS temp_embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT);"
    con.execute(sql_create_table)

    sql_create_table = "CREATE TABLE IF NOT EXISTS embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT NOT NULL, PRIMARY KEY (parent_class, parent_id, parent_version, class, id, version, ordr));"
    con.execute(sql_create_table)

    sql_create_table = "CREATE TABLE IF NOT EXISTS referencing (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, ref varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, ref, version, ordr));"
    con.execute(sql_create_table)

    # create_meta(db.con)

    if clean:
        con.execute("UPDATE meta SET embedding_last_modified = NULL;")
        con.execute("TRUNCATE embedded;")
        con.execute("TRUNCATE referencing;")

    if filter_clazz:
        filter_in = ', '.join(["'" + get_object_name(clazz) + "'" for clazz in filter_clazz])
        con.execute(f"DELETE FROM referencing WHERE parent_class IN ({filter_in});")

    con.begin()

    for clazz in set(filter_clazz).intersection(db.tables()) if filter_clazz else db.tables():
        # TODO: The DISTINCT here is actually a bug in the collection process, must investigate.
        objectname = get_object_name(clazz)
        try:
            con.execute(f"INSERT INTO temp_embedded SELECT DISTINCT CAST(z[1] AS TEXT), CAST(z[2] AS TEXT), CAST(z[3] AS TEXT), CAST(z[4] AS TEXT), CAST(z[5] AS TEXT), CAST(z[6] AS TEXT), CAST(z[7] AS INTEGER), CAST(z[8] AS TEXT) FROM (SELECT CAST(unnest(x) AS VARCHAR[]) AS z  FROM (SELECT embedding(object, '{objectname}') AS x FROM {objectname} WHERE COALESCE(last_modified < (SELECT COALESCE(embedding_last_modified, NOW()) FROM meta), TRUE)));")
        except Exception as err:
            print(f"failure in: {objectname} {err}")
            print(f"INSERT INTO temp_embedded SELECT DISTINCT CAST(z[1] AS TEXT), CAST(z[2] AS TEXT), CAST(z[3] AS TEXT), CAST(z[4] AS TEXT), CAST(z[5] AS TEXT), CAST(z[6] AS TEXT), CAST(z[7] AS INTEGER), CAST(z[8] AS TEXT) FROM (SELECT CAST(unnest(x) AS VARCHAR[]) AS z  FROM (SELECT embedding(object, '{objectname}') AS x FROM {objectname} WHERE COALESCE(last_modified < (SELECT COALESCE(embedding_last_modified, NOW()) FROM meta), TRUE)));")

            raise

    # con.execute("UPDATE meta SET embedding_last_modified = NOW();")

    con.execute("INSERT OR REPLACE INTO embedded SELECT DISTINCT * FROM temp_embedded WHERE path IS NOT NULL;")
    con.execute("INSERT OR REPLACE INTO referencing SELECT DISTINCT parent_class, parent_id, parent_version, \"class\", id, version, ordr FROM temp_embedded WHERE path IS NULL;")

    con.commit()

    sql_drop_table = f"DROP TABLE temp_embedded;"
    con.execute(sql_drop_table)

    con.remove_function('embedding')