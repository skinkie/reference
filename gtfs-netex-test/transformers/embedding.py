import functools
from typing import Generator

from netexio.database import Database
from netexio.dbaccess import recursive_attributes
from netexio.serializer import Serializer


def update_embedded_referencing(deserialized) -> Generator[list[str], None, None]:
    for obj, path in recursive_attributes(deserialized, []):
        if hasattr(obj, 'id'):
            if obj.id is not None:
                yield [
                    deserialized.__class__.__name__, deserialized.id, deserialized.version, obj.__class__.__name__,
                    obj.id,
                    obj.version if hasattr(obj, 'version') and obj.version is not None else 'any',
                    str(obj.order) if hasattr(obj, 'order') and obj.order is not None else '0',
                    '.'.join([str(s) for s in path])]

        elif hasattr(obj, 'ref'):
            if obj.ref is not None:
                if obj.name_of_ref_class is None:
                    # Hack, because NeTEx does not define the default name of ref class yet
                    if obj.__class__.__name__.endswith('RefStructure'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                    elif obj.__class__.__name__.endswith('Ref'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-3]

                yield [
                    deserialized.__class__.__name__, deserialized.id, deserialized.version, obj.name_of_ref_class,
                    obj.ref,
                    obj.version if hasattr(obj, 'version') and obj.version is not None else 'any',
                    str(obj.order) if hasattr(obj, 'order') and obj.order is not None else '0']

def embedding_udf(serializer: Serializer, serialized: bytes, clazz: str) -> list[str]:
    deserialized = serializer.unmarshall(serialized, clazz)
    return [x for x in update_embedded_referencing(deserialized) if len(x) > 0]
    # return result

def embedding_update(db: Database):
    con = db.con
    con.create_function('embedding', functools.partial(embedding_udf, db.serializer), return_type=list[str])

    sql_create_table = f"CREATE TEMPORARY TABLE IF NOT EXISTS temp_embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT);"
    con.execute(sql_create_table)

    con.execute("TRUNCATE embedded;")
    con.execute("TRUNCATE referencing;")

    for objectname in db.serializer.clean_element_names:
        con.execute(f"INSERT INTO temp_embedded SELECT CAST(z[1] AS TEXT), CAST(z[2] AS TEXT), CAST(z[3] AS TEXT), CAST(z[4] AS TEXT), CAST(z[5] AS TEXT), CAST(z[6] AS TEXT), CAST(z[7] AS INTEGER), CAST(z[8] AS TEXT) FROM (SELECT CAST(unnest(x) AS VARCHAR[]) AS z  FROM (SELECT embedding(object, '{objectname}') AS x FROM {objectname}));")

    con.execute("INSERT INTO embedded SELECT * FROM temp_embedded WHERE path <> '';")
    con.execute("INSERT INTO referencing SELECT parent_class, parent_id, parent_version, \"class\", id, version, ordr FROM temp_embedded WHERE path == '';")

    sql_drop_table = f"DROP TABLE temp_embedded;"
    con.execute(sql_drop_table)

    con.remove_function('embedding')