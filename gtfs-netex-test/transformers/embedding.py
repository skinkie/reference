import functools
from typing import Generator

from netexio.database import Database
from netexio.dbaccess import update_embedded_referencing
from netexio.serializer import Serializer
from utils import get_object_name


def embedding_udf(serializer: Serializer, serialized: bytes, clazz: str) -> list[str]:
    deserialized = serializer.unmarshall(serialized, clazz)
    return [x for x in update_embedded_referencing(serializer, deserialized) if len(x) > 0]
    # return result

def embedding_update(db: Database, clean=False, filter_clazz=None):
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

    for clazz in (filter_clazz or db.tables()):
        # TODO: The DISTINCT here is actually a bug in the collection process, must investigate.
        objectname = get_object_name(clazz)
        try:
            con.execute(f"INSERT INTO temp_embedded SELECT DISTINCT CAST(z[1] AS TEXT), CAST(z[2] AS TEXT), CAST(z[3] AS TEXT), CAST(z[4] AS TEXT), CAST(z[5] AS TEXT), CAST(z[6] AS TEXT), CAST(z[7] AS INTEGER), CAST(z[8] AS TEXT) FROM (SELECT CAST(unnest(x) AS VARCHAR[]) AS z  FROM (SELECT embedding(object, '{objectname}') AS x FROM {objectname} WHERE COALESCE(last_modified < (SELECT COALESCE(embedding_last_modified, NOW()) FROM meta), TRUE)));")
        except Exception as err:
            print(f"failure in: {objectname} {err}")
            raise

    # con.execute("UPDATE meta SET embedding_last_modified = NOW();")

    con.execute("INSERT OR REPLACE INTO embedded SELECT DISTINCT * FROM temp_embedded WHERE path IS NOT NULL;")
    con.execute("INSERT OR REPLACE INTO referencing SELECT DISTINCT parent_class, parent_id, parent_version, \"class\", id, version, ordr FROM temp_embedded WHERE path IS NULL;")

    con.commit()

    sql_drop_table = f"DROP TABLE temp_embedded;"
    con.execute(sql_drop_table)

    con.remove_function('embedding')