import sys
from typing import T, List, Generator, Tuple

import duckdb
from duckdb.duckdb import CatalogException

from isal import igzip_threaded
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import netex
from netexio.attributes import resolve_attr
from mro_attributes import list_attributes
from netex import VersionFrameDefaultsStructure, VersionOfObjectRef, VersionOfObjectRefStructure, \
    EntityInVersionStructure, DataManagedObject, ResponsibilitySetRef, DataSourceRefStructure
from netexio.database import Database
from netexio.xmlserializer import MyXmlSerializer
from transformers.references import replace_with_reference_inplace
from utils import get_object_name, get_element_name_with_ns

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

# TODO: For all load_ functions filter by id + version, not only id

def create_meta(db: Database):
    sql_create_table = "CREATE TABLE IF NOT EXISTS meta (embedding_last_modified TIMESTAMP DEFAULT NULL);"
    db.con.execute(sql_create_table)

    db.con.execute("SELECT count(*) FROM meta;")
    count, = db.con.fetchall()[0]
    if count == 0:
        db.con.execute("INSERT INTO meta VALUES (NULL);")

def load_embedded(db: Database, clazz: T, filter, cursor=False):
    # TODO: maybe return something here, which includes *ALL* objects that are embedded within this object, so it does not have to be resolved anymore
    objectname = get_object_name(clazz)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        cur.execute(f"SELECT parent_id, parent_version, parent_class FROM embedded WHERE id = ? and class = ?;", (filter, objectname,))
    except:
        return []

    return [(parent_id, parent_version, parent_clazz,) for parent_id, parent_version, parent_clazz in cur.fetchall()]

def load_referencing(db: Database, clazz: T, filter, cursor=False):
    objectname = get_object_name(clazz)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        cur.execute(f"SELECT ref, version, class FROM referencing WHERE parent_id = ? and parent_class = ?;", (filter, objectname,))
    except:
        return []

    return [(ref, version, clazz,) for ref, version, clazz in cur.fetchall()]

def load_referencing_inwards(db: Database, clazz: T, filter, cursor=False):
    objectname = get_object_name(clazz)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        cur.execute(f"SELECT parent_id, parent_version, parent_class FROM referencing WHERE ref = ? and class = ?;", (filter, objectname,))
    except:
        return []

    return [(parent_id, parent_version, parent_clazz,) for parent_id, parent_version, parent_clazz in cur.fetchall()]



def load_local(db: Database, clazz: T, limit=None, filter=None, cursor=False, embedding=True, embedded_parent=False) -> List[T]:
    objectname = get_object_name(clazz)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {objectname} WHERE id = ?;", (filter,))
        elif limit is not None:
            cur.execute(f"SELECT object FROM {objectname} ORDER BY id LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {objectname} ORDER BY id;")
    except:
        pass
        # This is the situation where the objectname is not available at all in the catalogue
        if embedding:
            return list(load_embedded_transparent_generator(db, clazz, limit, filter, embedded_parent))
        else:
            return []

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = db.serializer.unmarshall(xml, clazz)
        objs.append(obj)

    if embedding:
        objs += list(load_embedded_transparent_generator(db, clazz, limit, filter, embedded_parent))

    return objs


def recursive_resolve(db: Database, parent, resolved, filter=None, filter_class=set([]), inwards=True, outwards=True):
    for x in resolved:
        if parent.id == x.id and parent.__class__ == x.__class__:
            return

    resolved.append(parent)

    if inwards and (filter is False or filter == parent.id or parent.__class__ in filter_class):
        resolved_parents = load_referencing_inwards(db, parent.__class__, filter=parent.id)
        if len(resolved_parents) > 0:
            for y in resolved_parents:
                already_done = False
                for x in resolved:
                    y_class = getattr(sys.modules['netex'], y[2])
                    if (y[0] == x.id and y_class == x.__class__) or y_class in filter_class:
                        already_done = True
                        break

                if not already_done:
                    resolved_objs = load_local(db, getattr(sys.modules['netex'], y[2]),
                                               filter=y[0], embedding=True, embedded_parent=True)
                    if len(resolved_objs) > 0:
                        recursive_resolve(db, resolved_objs[0], resolved, filter,
                                          filter_class, inwards, outwards)  # TODO: not only consider the first

    # In principle this would already take care of everything recursive_attributes could find, but now does it inwards.
    if outwards:
        resolved_parents = load_referencing(db, parent.__class__, filter=parent.id)
        if len(resolved_parents) > 0:
            for y in resolved_parents:
                already_done = False
                for x in resolved:
                    if y[0] == x.id and getattr(sys.modules['netex'], y[2]) == x.__class__:
                        already_done = True
                        break

                if not already_done:
                    resolved_objs = load_local(db, getattr(sys.modules['netex'], y[2]),
                                               filter=y[0], embedding=True, embedded_parent=True)
                    if len(resolved_objs) > 0:
                        recursive_resolve(db, resolved_objs[0], resolved, filter,
                                          filter_class, inwards, outwards)  # TODO: not only consider the first
        # else:
        #      print(f"Cannot resolve referencing {parent.id}")

        for obj in recursive_attributes(parent, []):
            if hasattr(obj, 'id'):
                continue

            elif hasattr(obj, 'name_of_ref_class'):
                if obj.name_of_ref_class is None:
                    # Hack, because NeTEx does not define the default name of ref class yet
                    if obj.__class__.__name__.endswith('RefStructure'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                    elif obj.__class__.__name__.endswith('Ref'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-3]

                if not hasattr(netex, obj.name_of_ref_class):
                    # hack for non-existing structures
                    log_all(logging.WARN, 'related_explorer',
                            f'No attribute found in module {netex} for {obj.name_of_ref_class}.')

                    continue

                clazz = getattr(netex, obj.name_of_ref_class)

                # TODO: do this via a hash function
                # if obj in resolved:
                #    continue
                already_done = False
                for x in resolved:
                    if obj.ref == x.id and clazz == x.__class__:
                        already_done = True
                        break

                if not already_done:
                    resolved_objs = load_local(db, clazz, filter=obj.ref, embedding=True, embedded_parent=True)
                    if len(resolved_objs) > 0:
                        recursive_resolve(db, resolved_objs[0], resolved, filter,
                                          filter_class, inwards, outwards)  # TODO: not only consider the first
                    else:
                        # print(obj.ref)
                        resolved_parents = load_embedded(db, clazz, filter=obj.ref)
                        if len(resolved_parents) > 0:
                            for y in resolved_parents:
                                already_done = False
                                for x in resolved:
                                    if y[0] == x.id and getattr(sys.modules['netex'], y[2]) == x.__class__:
                                        already_done = True
                                        break

                                if not already_done:
                                    resolved_objs = load_local(db, getattr(sys.modules['netex'], y[2]), filter=y[0],
                                                               embedding=True, embedded_parent=True)
                                    if len(resolved_objs) > 0:
                                        recursive_resolve(db, resolved_objs[0], resolved, filter,
                                                          filter_class, inwards, outwards)  # TODO: not only consider the first
                        else:
                            log_all(logging.WARN, 'related_explorer', f"Cannot resolve embedded {obj.ref}")


object_cache = {}


def fetch_references_classes_generator(db: Database, db2: Database, classes: list):
    cur = db.cursor()
    cur2 = db2.cursor()

    list_classes = ', '.join([f"'{get_object_name(clazz)}'" for clazz in classes])
    processed = set()

    # Find all embeddings and objects the target profile, elements must not be added directly later, but referenced.
    query = "SELECT DISTINCT class, id, version FROM embedded;"
    cur2.execute(query)
    existing_ids = {(clazz, ref, version,) for clazz, ref, version in cur2.fetchall()}

    for clazz in classes:
        objectname = get_object_name(clazz)
        query = f"SELECT DISTINCT id, version FROM {objectname}"
        try:
            cur2.execute(query)
            set2 = {(objectname, id, version,) for id, version in cur2.fetchall()}
            existing_ids = existing_ids.union(set2)
        except duckdb.duckdb.CatalogException:
            pass

    print(".")

    # Practically this could still lead to a reference from an embedded class, which may already be included
    # (or not, hence we would need to assure that those objects are not in the class list)
    query = f"SELECT DISTINCT class, ref, version FROM referencing WHERE class NOT IN ({list_classes}) ORDER BY class;"
    print(query)
    cur2.execute(query)
    while True:
        result = cur2.fetchone()
        if result is None:
            break
        clazz, ref, version = result

        # TODO: we cannot trust SQL objectname
        results = load_local(db, getattr(sys.modules['netex'], clazz), limit=1, filter=ref, cursor=True, embedding=True, embedded_parent=True)
        if len(results) > 0:
            needle = get_object_name(results[0].__class__) + '|' + results[0].id
            if results[0].__class__ in classes: # Don't export classes, which are part of the main delivery
                pass
            elif needle in processed: # Don't export classes which have been exported already, maybe this can be solved at the database layer
                pass
            else:
                processed.add(needle)

                yield results[0]

                # An element may obviously also include other references.
                resolved = []
                filter_set = {results[0].__class__}.union(classes)
                recursive_resolve(db, results[0], resolved, results[0].id, filter_set, False, True)

                for resolve in resolved:
                    needle = get_object_name(resolve.__class__) + '|' + resolve.id
                    if resolve.__class__ in classes:  # Don't export classes, which are part of the main delivery
                        pass
                    elif needle in processed:  # Don't export classes which have been exported already, maybe this can be solved at the database layer
                        pass
                    else:
                        processed.add(needle)
                        # We can do two things here, query the database for embeddings, or recursively iterate over the object.

                        query = "SELECT DISTINCT class, id, version, path FROM embedded WHERE parent_class = ? AND parent_id = ? AND parent_version = ?;"
                        cur.execute(query, (get_object_name(resolve.__class__), resolve.id, resolve.version,)) # TODO: change to meta

                        for clazz, id, version, path in cur.fetchall():
                            if (clazz, id, version,) in existing_ids:
                                replace_with_reference_inplace(resolve, path)

                        yield resolve

                # TODO: The problem may be here that an embedding of this class, has been made a first class object, or an embedding of an existing element.


def load_generator(db: Database, clazz: T, limit=None, filter=None, embedding=True):
    objectname = get_object_name(clazz)

    cur = db.cursor()
    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {objectname} WHERE id = ?;", (filter,))
        elif limit is not None:
            cur.execute(f"SELECT object FROM {objectname} ORDER BY id LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {objectname} ORDER BY id;")
    except:
        pass
        if embedding:
            yield from load_embedded_transparent_generator(db, clazz, limit, filter)
        return

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield db.serializer.unmarshall(xml[0], clazz)

    if embedding:
        yield from load_embedded_transparent_generator(db, clazz, limit, filter)

object_cache = {}



def load_embedded_transparent_generator(db: Database, clazz: T, limit=None, filter=None, parent=False) -> List[T]:
    objectname = get_object_name(clazz)

    cur = db.cursor()
    try:
        if filter is not None:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded WHERE id = ? and class = ?;", (filter, objectname,))
        elif limit is not None:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded WHERE class = ? ORDER BY id LIMIT ?;", (objectname, limit,))
        else:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded WHERE class = ? ORDER BY id;", (objectname,))
    except:
        return

    try:
        cur2 = db.cursor()
        while True:
            result = cur.fetchone()
            if result is None:
                break

            parent_id, parent_version, parent_clazz, path = result
            needle = '|'.join([parent_id, parent_version, parent_clazz])

            if needle not in object_cache:
                cur2.execute(f"SELECT object FROM {parent_clazz} WHERE id = ? AND version = ? ORDER BY id LIMIT 1;", (parent_id, parent_version,))
                object = cur2.fetchone()
                true_parent_clazz = db.serializer.interesting_classes(db.serializer.clean_element_names.index(parent_clazz))
                object_cache[needle] = db.serializer.unmarshall(object[0], true_parent_clazz)

            obj = object_cache[needle]
            if obj is not None:
                if parent:
                    yield obj

                else:
                    # TODO: separate function
                    split = []
                    for p in path.split('.'):
                        if p.isnumeric():
                            p = int(p)
                        split.append(p)
                    yield resolve_attr(obj, split)

    except TypeError:
        pass

from lxml import etree
def load_lxml_generator(con, clazz, limit=None):
    objectname = get_object_name(clazz)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {objectname} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {objectname};")

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield etree.fromstring(xml[0])

def write_lxml_generator(db: Database, clazz, generator: Generator):
    objectname = get_object_name(clazz)

    cur = db.cursor()
    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], obj.attrib['version'], obj.attrib['order'], etree.tostring(obj, encoding="unicode")
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], obj.attrib['version'], etree.tostring(obj, encoding="unicode")
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], etree.tostring(obj, encoding="unicode")
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', _prepare3(generator, objectname))
    else:
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', _prepare2(generator, objectname))

    print('\n')

def get_single(db: Database, clazz: T, id, version=None, cursor=False) -> T:
    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    objectname = get_object_name(clazz)

    try:
        if version == 'any' or version is None:
            cur.execute(f"SELECT object FROM {objectname} WHERE id = ? ORDER BY version DESC LIMIT 1;", (id,))
        else:
            cur.execute(f"SELECT object FROM {objectname} WHERE id = ? AND version = ? LIMIT 1;", (id, version,))
    except:
        pass
        return

    row = cur.fetchone()
    if row is not None:
        obj = db.serializer.unmarshall(row[0], clazz)
        return obj


def write_objects(db: Database, objs, empty=False, many=False, silent=False, cursor=False):
    if len(objs) == 0:
        return

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    clazz = objs[0].__class__
    objectname = get_object_name(clazz)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id));"


    print(sql_create_table)
    cur.execute(sql_create_table)

    try:
        if many:
            print(objectname, len(objs))
            if hasattr(clazz, 'order'):
                cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', [(obj.id, obj.version, obj.order, db.serializer.marshall(obj, objectname)) for obj in objs])
            elif hasattr(clazz, 'version'):
                cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', [(obj.id, obj.version, db.serializer.marshall(obj, objectname)) for obj in objs])
            else:
                cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());',
                                [(obj.id, db.serializer.marshall(obj, objectname)) for obj in objs])
        else:
            for i in range(0, len(objs)):
                obj = objs[i]
                if hasattr(clazz, 'order'):
                    cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', (obj.id, obj.version, obj.order, db.serializer.marshall(obj, objectname)))
                elif hasattr(clazz, 'version'):
                    cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', (obj.id, obj.version, db.serializer.marshall(obj, objectname)))
                else:
                    cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', (obj.id, db.serializer.marshall(obj, objectname)))

                if not silent:
                    if i % 13 == 0:
                        print('\r', objectname, str(i), end = '')
        if not silent:
            print('\r', objectname, len(objs), end='')
    except:
        raise
        # pass


def write_generator(db: Database, clazz, generator: Generator, empty=False):
    cur = db.cursor()
    objectname = get_object_name(clazz)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, obj.order, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare4(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare3(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', _prepare3(generator, objectname))
    else:
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare2(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', _prepare2(generator, objectname))

    print('\n')

def copy_table(db_read: Database, db_write: Database, classes: list, clean=False):
    if db_read.read_only:
        db_write.con.execute(f"ATTACH IF NOT EXISTS '{db_read.database_file}' AS db_read (READ_ONLY);")
        for clazz in classes:
            objectname = get_object_name(clazz)
            try:
                if clean:
                    db_write.con.execute(f'DROP TABLE IF EXISTS {objectname};')

                sql_create_table = create_table_sql(db_write, clazz)
                db_write.con.execute(sql_create_table)
                db_write.con.execute(f'INSERT OR REPLACE INTO {objectname} SELECT * FROM db_read.{objectname};')
            except CatalogException:
                pass

        db_write.con.execute(f"DETACH db_read;")

    else:
        for clazz in classes:
            try:
                if clean:
                    objectname = get_object_name(clazz)
                    db_write.con.execute(f'DROP TABLE IF EXISTS {objectname};')

                write_generator(db_write, clazz, load_generator(db_read, clazz, embedding=False))
            except CatalogException:
                pass

def create_table_sql(db: Database, clazz: T) -> str:
    objectname = get_object_name(clazz)
    optionals = {x[0]: x[1][1] for x in list_attributes(clazz) if x[0] in ('order', 'version')}
    ordr_opt = optionals.get('order', False)
    version_opt = optionals.get('version', False)

    if hasattr(clazz, 'order'):
        if ordr_opt:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version));"
        else:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version, ordr));"

    elif hasattr(clazz, 'version'):
        if version_opt:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64), object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id));"
        else:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id, version));"

    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL, PRIMARY KEY (id));"

    return sql_create_table

def update_generator(db: Database, clazz, generator: Generator):
    cur = db.cursor()
    objectname = get_object_name(clazz)

    # This is not used effectively at this point, considering that DuckDB's ATTACH is not persistent
    # https://github.com/duckdb/duckdb-web/issues/3495
    cur.execute(f"SELECT table_type FROM information_schema.tables WHERE table_name = '{objectname}';")
    result = cur.fetchone()
    if result:
        if result[0] == 'VIEW':
            cur.execute(f"ALTER VIEW {objectname} RENAME TO x{objectname};")
            cur.execute(f"CREATE TABLE {objectname} AS SELECT * FROM x{objectname};")
            cur.execute(f"DROP VIEW x{objectname};")
        else:
            # In this case it already exists.
            pass

    else:
        sql_create_table = create_table_sql(db, clazz)
        cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, obj.order, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, db.serializer.marshall(obj, objectname)
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare4(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare3(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());', _prepare3(generator, objectname))
    else:
        if cur.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare2(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, object, last_modified) VALUES (?, ?, NOW());', _prepare2(generator, objectname))

    print('\n')

def get_interesting_classes(filter=None):
    import inspect
    import netex

    # Get all classes from the generated NeTEx Python Dataclasses
    clsmembers = inspect.getmembers(netex, inspect.isclass)

    # The interesting class members certainly will have a "Meta class" with a namespace
    interesting_members = [x for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace')]

    # Specifically we are interested in classes that are derived from "EntityInVersion", to find them, we exclude embedded child objects called "VersionedChild"
    entitiesinversion = [x for x in interesting_members if netex.VersionedChildStructure not in x[1].__mro__ and netex.EntityInVersionStructure in x[1].__mro__]

    # Obviously we want to have the VersionedChild too
    versionedchild = [x for x in interesting_members if netex.VersionedChildStructure in x[1].__mro__]

    # There is one particular container in NeTEx that should reflect almost the same our collection EntityInVersion namely the "GeneralFrame"
    general_frame_members = netex.GeneralFrameMembersRelStructure.__dataclass_fields__['choice'].metadata['choices']

    # The interesting part here is where the difference between the two lie.
    # geme = [x['type'].Meta.getattr('name', x['type'].__name__) for x in general_frame_members]
    # envi = [x[0] for x in entitiesinversion]
    # set(geme) - set(envi)

    if filter is not None:
        clean_element_names = [x[0] for x in entitiesinversion if x[0] in filter]
        interesting_element_names =  [get_element_name_with_ns(x[1]) for x in entitiesinversion if x[0] in filter]
        interesting_clazzes = [x[1] for x in entitiesinversion if x[0] in filter]
    else:
        clean_element_names = [x[0] for x in entitiesinversion if not x[0].endswith('Frame')]
        interesting_element_names =  [get_element_name_with_ns(x[1]) for x in entitiesinversion if not x[0].endswith('Frame')]
        interesting_clazzes = [x[1] for x in entitiesinversion if not x[0].endswith('Frame')]

    return clean_element_names, interesting_element_names, interesting_clazzes

def setup_database(db: Database, classes, clean=False, cursor=False):
    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    clean_element_names, interesting_element_names, interesting_classes = classes

    if clean:
        for clazz in interesting_classes:
            objectname = get_object_name(clazz)
            sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
            cur.execute(sql_drop_table)
        cur.execute("VACUUM;")

    sql_create_table = f"CREATE TABLE IF NOT EXISTS embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT NOT NULL, PRIMARY KEY (parent_class, parent_id, parent_version, class, id, version, ordr));"
    print(sql_create_table)
    cur.execute(sql_create_table)

    sql_create_table = f"CREATE TABLE IF NOT EXISTS referencing (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, ref varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, ref, version, ordr));"
    print(sql_create_table)
    cur.execute(sql_create_table)

    create_meta(db)

    for clazz in interesting_classes:
        sql_create_table = create_table_sql(db, clazz)
        print(sql_create_table)
        cur.execute(sql_create_table)

def get_local_name(element):
    if hasattr(element, 'Meta') and hasattr(element.Meta, 'name'):
        return element.Meta.name
    return element.__name__


def update_embedded_referencing(deserialized) -> Generator[list[str], None, None]:
    for obj, path in recursive_attributes(deserialized, []):
        if hasattr(obj, 'id'):
            if obj.id is not None:
                yield [
                    get_object_name(deserialized.__class__), deserialized.id, deserialized.version, get_object_name(obj.__class__),
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
                    get_object_name(deserialized.__class__), deserialized.id, deserialized.version, obj.name_of_ref_class,
                    obj.ref,
                    obj.version if hasattr(obj, 'version') and obj.version is not None else 'any',
                    str(obj.order) if hasattr(obj, 'order') and obj.order is not None else '0', None]

"""
def update_embedded_referencing(con, object, inner_loop=None):
    sql_insert_embedded = "INSERT OR REPLACE INTO embedded (parent_class, parent_id, parent_version, class, id, version, ordr, path) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
    sql_insert_reference = "INSERT OR REPLACE INTO referencing (parent_class, parent_id, parent_version, class, ref, version, ordr) VALUES (?, ?, ?, ?, ?, ?, ?);"

    for obj, path in recursive_attributes(object, []):
        if inner_loop:
            inner_loop(obj, path)

        if hasattr(obj, 'id'):
            if obj.id is not None:
                con.execute(sql_insert_embedded, (
                object.__class__.__name__, object.id, object.version, obj.__class__.__name__, obj.id,
                obj.version if hasattr(obj, 'version') and obj.version is not None else 'any', obj.order if hasattr(obj, 'order') and obj.order is not None else 0,
                '.'.join([str(s) for s in path])))
        elif hasattr(obj, 'ref'):
            if obj.ref is not None:
                if obj.name_of_ref_class is None:
                    # Hack, because NeTEx does not define the default name of ref class yet
                    if obj.__class__.__name__.endswith('RefStructure'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                    elif obj.__class__.__name__.endswith('Ref'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-3]

                con.execute(sql_insert_reference, (
                object.__class__.__name__, object.id, object.version, obj.name_of_ref_class, obj.ref,
                obj.version if hasattr(obj, 'version') and obj.version is not None else 'any', obj.order if hasattr(obj, 'order') and obj.order is not None else 0))
"""

def insert_database(db: Database, classes, f=None, type_of_frame_filter=None, cursor=False):
    xml_serializer = MyXmlSerializer()
    clsmembers = inspect.getmembers(netex, inspect.isclass)
    all_frames = [get_local_name(x[1]) for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace') and netex.VersionFrameVersionStructure in x[1].__mro__]

    # See: https://github.com/NeTEx-CEN/NeTEx/issues/788
    # all_datasource_refs = [x[0] for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace') and hasattr(x[1], 'data_source_ref_attribute')]
    all_datasource_refs = [get_local_name(x[1]) for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace') and netex.DataManagedObjectStructure  in x[1].__mro__]
    all_responsibility_set_refs = [get_local_name(x[1]) for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace') and netex.EntityInVersionStructure  in x[1].__mro__]
    all_srs_name = [get_local_name(x[1]) for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1], 'srs_name')]

    frame_defaults_stack = []
    if f is None:
        return

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    # sql_create_table = "CREATE TABLE IF NOT EXISTS temp_embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT);"
    # cur.execute(sql_create_table)

    clean_element_names, interesting_element_names, interesting_classes = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        clazz_by_name[interesting_element_names[i]] = interesting_classes[i]

    events = ("start", "end")
    context = etree.iterparse(f, events=events, remove_blank_text=True)
    current_element_tag = None
    current_framedefaults = None
    current_datasource_ref = None
    current_responsibility_set_ref = None
    current_location_system = None
    skip_frame = False

    location_srsName = None
    for event, element in context:
        localname = element.tag.split('}')[-1]  # localname

        if event == 'start':
            if current_element_tag is None and element.tag in interesting_element_names:
                current_element_tag = element.tag

            elif localname == 'TypeOfFrameRef':
                if type_of_frame_filter is not None and element.attrib['ref'] not in type_of_frame_filter:
                    # TODO: log a single warning that an unknown TypeOfFrame is found, and is not processed
                    print(f"{element.attrib['ref']} is not a known TypeOfFrame")
                    skip_frame = True

            if localname in all_frames:
                frame_defaults_stack.append(None)

            elif localname == 'Location':
                if 'srsName' in element.attrib:
                    location_srsName = element.attrib['srsName']

        elif event == 'end':
            # current_element_tag = element.tag
            if localname == 'FrameDefaults':
                xml = etree.tostring(element, encoding='unicode')
                frame_defaults: VersionFrameDefaultsStructure = parser.from_string(xml, VersionFrameDefaultsStructure)
                frame_defaults_stack[-1] = frame_defaults
                current_framedefaults = frame_defaults
                if current_framedefaults.default_data_source_ref is not None:
                    current_datasource_ref = current_framedefaults.default_data_source_ref.ref
                if current_framedefaults.default_responsibility_set_ref is not None:
                    current_responsibility_set_ref = current_framedefaults.default_responsibility_set_ref.ref
                if current_framedefaults.default_location_system is not None:
                    current_location_system = current_framedefaults.default_location_system

                continue

            elif localname in all_frames:
                # This is the end of the frame, pop the frame_defaults stack
                frame_defaults_stack.pop()
                filtered = [fd for fd in frame_defaults_stack if fd is not None]
                current_framedefaults = filtered[-1] if len(filtered) > 0 else None

                current_datasource_ref = None
                current_responsibility_set_ref = None
                current_location_system = None
                for fd in reversed(filtered):
                    if current_datasource_ref is None:
                        if fd.default_data_source_ref is not None:
                            current_datasource_ref = fd.default_data_source_ref.ref
                    if current_responsibility_set_ref is None:
                        if fd.default_responsibility_set_ref is not None:
                            current_responsibility_set_ref = fd.default_responsibility_set_ref.ref
                    if current_location_system is None:
                        if fd.default_location_system is not None:
                            current_location_system = fd.default_location_system

                skip_frame = False
                continue

            if skip_frame:
               continue

            if current_framedefaults is not None:
                if current_datasource_ref is not None and localname in all_datasource_refs:
                    if 'dataSourceRef' not in element.attrib:
                        element.attrib['dataSourceRef'] = current_datasource_ref

                if current_responsibility_set_ref is not None and localname in all_responsibility_set_refs:
                    if 'responsibilitySetRef' not in element.attrib:
                        element.attrib['responsibilitySetRef'] = current_responsibility_set_ref

                if current_location_system is not None:
                    if localname in all_srs_name:
                        if 'srsName' not in element.attrib:
                            element.attrib['srsName'] = location_srsName if location_srsName is not None else current_location_system

                    if localname == 'Location':
                        if 'srsName' not in element.attrib:
                            element.attrib['srsName'] = current_location_system

                        location_srsName = None

            if current_element_tag == element.tag: # https://stackoverflow.com/questions/65935392/why-does-elementtree-iterparse-sometimes-retrieve-xml-elements-incompletely
                if 'id' not in element.attrib:
                    current_element_tag = None
                    # print(xml)
                    continue

                clazz = clazz_by_name[element.tag]

                id = element.attrib['id']

                version = element.attrib.get('version', None)
                order = element.attrib.get('order', None)
                object = xml_serializer.unmarshall(element, clazz)

                if hasattr(clazz, 'order'):
                    sql_insert_object = f"""INSERT OR REPLACE INTO {localname} (id, version, ordr, object, last_modified) VALUES (?, ?, ?, ?, NOW());"""
                    try:
                        cur.execute(sql_insert_object, (id, version, order, db.serializer.marshall(object, clazz),))
                    except:
                        print(etree.tostring(element))
                        raise
                        pass

                elif hasattr(clazz, 'version'):
                    sql_insert_object = f"""INSERT OR REPLACE INTO {localname} (id, version, object, last_modified) VALUES (?, ?, ?, NOW());"""
                    try:
                        cur.execute(sql_insert_object, (id, version, db.serializer.marshall(object, clazz),))
                    except:
                        print(etree.tostring(element))
                        raise
                        pass

                else:
                    sql_insert_object = f"""INSERT OR REPLACE INTO {localname} (id, object, last_modified) VALUES (?, ?, NOW());"""
                    try:
                        cur.execute(sql_insert_object, (id, db.serializer.marshall(object, clazz),))
                    except:
                        print(etree.tostring(element))
                        raise
                        pass

                current_element_tag = None

                # WARNING: Executing the following code is SLOWER than deserialisation of our entire database, in the UDF. Factor 4x

                # l = [x for x in update_embedded_referencing(object) if len(x) > 0]
                # if len(l) > 0:
                #    cur.executemany("INSERT INTO temp_embedded VALUES (?, ?, ?, ?, ?, ?, ?, ?)", l)

    # For this to work, we must expect that the caller always updates the added objects.
    # cur.execute("UPDATE meta SET embedding_last_modified = NOW();")

    # cur.execute("INSERT OR REPLACE INTO embedded SELECT DISTINCT * FROM temp_embedded WHERE path IS NOT NULL;")
    # cur.execute("INSERT OR REPLACE INTO referencing SELECT DISTINCT parent_class, parent_id, parent_version, \"class\", id, version, ordr FROM temp_embedded WHERE path IS NULL;")

    # cur.execute("DROP TABLE temp_embedded;")


def recursive_attributes(obj, depth: List[int]) -> Tuple[object, List[int]]:
    # qprint(obj.__class__.__name__)
    if issubclass(obj.__class__, EntityInVersionStructure) and obj.data_source_ref_attribute is not None:
        yield DataSourceRefStructure(ref=obj.data_source_ref_attribute), depth + ['data_source_ref_attribute']
    if issubclass(obj.__class__, DataManagedObject) and obj.responsibility_set_ref_attribute is not None:
        yield ResponsibilitySetRef(ref=obj.responsibility_set_ref_attribute), depth + ['responsibility_set_ref_attribute']

    mydepth = depth.copy()
    mydepth.append(0)
    for key in obj.__dict__.keys():
        mydepth[-1] = key
        v = obj.__dict__.get(key, None)
        if v is not None:
            # print(v)
            if issubclass(v.__class__, VersionOfObjectRef) or issubclass(v.__class__, VersionOfObjectRefStructure):
                yield v, mydepth

            else:
                if (v.__class__.__name__ in netex.__all__ and hasattr(v, '__dict__')):
                    if hasattr(v, 'id'):
                        yield v, mydepth
                    yield from recursive_attributes(v, mydepth)
                elif v.__class__ in (list, tuple):
                    mydepth.append(0)
                    for j in range(0, len(v)):
                        mydepth[-1] = j
                        x = v[j]
                        if x is not None:
                            if issubclass(x.__class__, VersionOfObjectRef) or issubclass(x.__class__,
                                                                                         VersionOfObjectRefStructure):
                                yield x, mydepth
                            elif (x.__class__.__name__ in netex.__all__ and hasattr(x, '__dict__')):
                                if hasattr(x, 'id'):
                                    yield x, mydepth
                                yield from recursive_attributes(x, mydepth)
                    mydepth.pop()

import inspect

def resolve_all_references(con, classes, cursor=False):
    all_class_names = {name for name, obj in inspect.getmembers(netex) if inspect.isclass(obj)}

    if cursor:
        cur = con.cursor()
    else:
        cur = con

    # TODO: This pattern must be able to make generic, and maybe even avoided running multiple times
    clean_element_names, interesting_element_names, interesting_classes = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        clazz_by_name[interesting_element_names[i]] = interesting_classes[i]

    cur.execute("SET wal_autocheckpoint='1TB';")
    sql_create_table = f"CREATE TABLE IF NOT EXISTS referencing (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, ref varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, ref, version, ordr));"
    print(sql_create_table)
    cur.execute(sql_create_table)
    cur.execute("TRUNCATE referencing;")

    for clazz in clazz_by_name.values():
        print(clazz)
        for parent in load_generator(con, clazz):
            print(parent.id)
            for obj in recursive_attributes(parent):
                if obj.name_of_ref_class is None:
                    # Hack, because NeTEx does not define the default name of ref class yet
                    # TODO: #147
                    if obj.__class__.__name__.endswith('RefStructure'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                    elif obj.__class__.__name__.endswith('Ref'):
                        obj.name_of_ref_class = obj.__class__.__name__[0:-3]


                if obj.name_of_ref_class not in all_class_names:
                # if not hasattr(netex, obj.name_of_ref_class):
                    # hack for non-existing structures
                    print(f'No attribute found in module {netex} for {obj.name_of_ref_class}.')
                    continue

                if hasattr(obj, 'order'):
                    order = obj.order
                else:
                    order = 0


                sql_insert_object = "INSERT OR REPLACE INTO referencing (parent_class, parent_id, parent_version, class, ref, version, ordr) VALUES (?, ?, ?, ?, ?, ?, ?);"
                try:
                    cur.execute(sql_insert_object, (get_object_name(parent.__class__), parent.id, parent.version, obj.name_of_ref_class, obj.ref, obj.version or 'any', order))
                except duckdb.duckdb.ConstraintException:
                    pass

        cur.execute("CHECKPOINT;")


# TODO: This is a duplicate, maybe clean up at all other places, and just do everything here
def resolve_all_references_and_embeddings(con, classes, cursor=False):
    all_class_names = {name for name, obj in inspect.getmembers(netex) if inspect.isclass(obj)}

    if cursor:
        cur = con.cursor()
    else:
        cur = con

    # TODO: This pattern must be able to make generic, and maybe even avoided running multiple times
    clean_element_names, interesting_element_names, interesting_classes = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        clazz_by_name[interesting_element_names[i]] = interesting_classes[i]

    cur.execute("SET wal_autocheckpoint='1TB';")
    sql_create_table = f"CREATE TABLE IF NOT EXISTS referencing (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, ref varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, ref, version, ordr));"
    cur.execute(sql_create_table)
    cur.execute("TRUNCATE referencing;")

    sql_create_table = f"CREATE TABLE IF NOT EXISTS embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, id, version, ordr));"
    cur.execute(sql_create_table)
    cur.execute("TRUNCATE embedded;")


    for clazz in clazz_by_name.values():
        print(clazz)
        for parent in load_generator(con, clazz, embedding=False):
            # print(parent.id)
            count = 0
            for obj in recursive_attributes(parent):
                if hasattr(obj, 'id'):
                    if obj.id is not None:
                        version =  obj.version if hasattr(obj, 'version') and obj.version is not None else 'any'
                        order = obj.order if hasattr(obj, 'order') and obj.order is not None else 0

                        sql_insert_object = "INSERT INTO embedded (parent_class, parent_id, parent_version, class, id, version, ordr) VALUES (?, ?, ?, ?, ?, ?, ?);"
                        try:
                            cur.execute(sql_insert_object, (
                            get_object_name(clazz), parent.id, parent.version, get_object_name(obj.__class__), obj.id, version, order))
                        except:
                            raise

                else:
                    if obj.name_of_ref_class is None:
                        # Hack, because NeTEx does not define the default name of ref class yet
                        if obj.__class__.__name__.endswith('RefStructure'):
                            obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                        elif obj.__class__.__name__.endswith('Ref'):
                            obj.name_of_ref_class = obj.__class__.__name__[0:-3]


                    if obj.name_of_ref_class not in all_class_names:
                    # if not hasattr(netex, obj.name_of_ref_class):
                        # hack for non-existing structures
                        print(f'No attribute found in module {netex} for {obj.name_of_ref_class}.')
                        continue

                    if hasattr(obj, 'order'):
                        order = obj.order
                    else:
                        order = 0


                    sql_insert_object = "INSERT OR REPLACE INTO referencing (parent_class, parent_id, parent_version, class, ref, version, ordr) VALUES (?, ?, ?, ?, ?, ?, ?);"
                    try:
                        cur.execute(sql_insert_object, (get_object_name(parent.__class__), parent.id, parent.version, obj.name_of_ref_class, obj.ref, obj.version or 'any', order))
                    except duckdb.duckdb.ConstraintException:
                        pass

                    if count == 1000:
                        cur.execute("CHECKPOINT;")
                        count = 0

                    count += 1

        cur.execute("CHECKPOINT;")


def attach_objects(con, read_database: str, clazz: T):
    objectname = get_object_name(clazz)
    # con.execute(f"DROP TABLE IF EXISTS {type};")
    # con.execute(f"CREATE VIEW {type} AS SELECT * FROM original.{type};")

    # Workaround for https://github.com/duckdb/duckdb-web/issues/3495
    attach_source(con, read_database)
    con.execute(f"INSERT INTO {objectname} SELECT * FROM original.{objectname};")

def attach_source(con, read_database: str):
    con.execute(f"ATTACH IF NOT EXISTS '{read_database}' AS original (READ_ONLY);")

def open_netex_file(filename):
    if filename.endswith('.xml.gz'):
        yield igzip_threaded.open(filename, 'rb', compresslevel=3, threads=3)
    elif filename.endswith('.xml'):
        yield open(filename, 'rb')
    elif filename.endswith('.zip'):
        import zipfile
        zip = zipfile.ZipFile(filename)
        for zipfilename in zip.filelist:
            l_zipfilename = zipfilename.filename.lower()
            if l_zipfilename.endswith('.xml.gz') or l_zipfilename.endswith('.xml'):
                yield zip.open(zipfilename)

