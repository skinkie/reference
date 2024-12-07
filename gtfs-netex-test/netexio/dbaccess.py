import inspect
import sys
from typing import T, List, Generator, Tuple

import duckdb

from isal import igzip_threaded
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import netex
from mro_attributes import list_attributes
from netex import VersionFrameDefaultsStructure, VersionOfObjectRef, VersionOfObjectRefStructure, \
    EntityInVersionStructure, DataSourceRef, DataManagedObject, ResponsibilitySetRef, DataSourceRefStructure
from netexio.database import Database
from netexio.xmlserializer import MyXmlSerializer

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

# serializer_config = SerializerConfig(ignore_default_attributes=True)
# serializer_config.indent = None
# serializer_config.xml_declaration = False
# serializer_config.ignore_default_attributes = True
# serializer = XmlSerializer(config=serializer_config)
# serializer.encoding = 'utf-8'

# TODO: For all load_ functions filter by id + version, not only id

def load_embedded(con, clazz: T, filter, cursor=False):
    # TODO: maybe return something here, which includes *ALL* objects that are embedded within this object, so it does not have to be resolved anymore
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    if cursor:
        cur = con.cursor()
    else:
        cur = con

    try:
        cur.execute(f"SELECT parent_id, parent_version, parent_class FROM embedded WHERE id = ? and class = ?;", (filter, type,))
    except:
        return []

    return [(parent_id, parent_version, parent_clazz,) for parent_id, parent_version, parent_clazz in cur.fetchall()]

def load_referencing(db: Database, clazz: T, filter, cursor=False):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        cur.execute(f"SELECT ref, version, class FROM referencing WHERE parent_id = ? and parent_class = ?;", (filter, type,))
    except:
        return []

    return [(ref, version, clazz,) for ref, version, clazz in cur.fetchall()]

def load_referencing_inwards(db: Database, clazz: T, filter, cursor=False):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        cur.execute(f"SELECT parent_id, parent_version, parent_class FROM referencing WHERE ref = ? and class = ?;", (filter, type,))
    except:
        return []

    return [(parent_id, parent_version, parent_clazz,) for parent_id, parent_version, parent_clazz in cur.fetchall()]


def load_local(db: Database, clazz: T, limit=None, filter=None, cursor=False, embedding=True) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
        elif limit is not None:
            cur.execute(f"SELECT object FROM {type} ORDER BY id LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {type} ORDER BY id;")
    except:
        pass
        # This is the situation where the type is not available at all in the catalogue
        if embedding:
            return list(load_embedded_transparent_generator(db, clazz, limit, filter))
        else:
            return []

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = db.serializer.unmarshall(xml, type)
        objs.append(obj)

    if embedding:
        objs += list(load_embedded_transparent_generator(db, clazz, limit, filter))

    return objs

def load_generator(db: Database, clazz, limit=None, filter=None, embedding=True):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = db.cursor()
    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
        elif limit is not None:
            cur.execute(f"SELECT object FROM {type} ORDER BY id LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {type} ORDER BY id;")
    except:
        pass
        if embedding:
            yield from load_embedded_transparent_generator(db, clazz, limit, filter)
        return

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield db.serializer.unmarshall(xml[0], type)

    if embedding:
        yield from load_embedded_transparent_generator(db, clazz, limit, filter)

object_cache = {}

# Alternative implementation for attrgetter, handles list indices
# from operator import attrgetter
def resolve_attr(obj, attr):
    for name in attr:
        if isinstance(name, int):
            obj = obj[name]
        else:
            obj = getattr(obj, name)
    return obj

def load_embedded_transparent_generator(db: Database, clazz: T, limit=None, filter=None) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = db.cursor()
    try:
        if filter is not None:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded WHERE id = ? and class = ?;", (filter, type,))
        elif limit is not None:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded ORDER BY id LIMIT ?;", (limit,))
        else:
            cur.execute(f"SELECT DISTINCT parent_id, parent_version, parent_class, path FROM embedded WHERE class = ? ORDER BY id;", (type,))
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
                object_cache[needle] = db.serializer.unmarshall(object[0], parent_clazz)

            obj = object_cache[needle]
            if obj is not None:
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
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield etree.fromstring(xml[0])

def write_lxml_generator(db: Database, clazz, generator: Generator):
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = db.cursor()
    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id));"

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

    type = getattr(clazz.Meta, 'name', clazz.__name__)

    try:
        if version == 'any' or version is None:
            cur.execute(f"SELECT object FROM {type} WHERE id = ? ORDER BY version DESC LIMIT 1;", (id,))
        else:
            cur.execute(f"SELECT object FROM {type} WHERE id = ? AND version = ? LIMIT 1;", (id, version,))
    except:
        pass
        return

    row = cur.fetchone()
    if row is not None:
        obj = db.serializer.unmarshall(row[0], type)
        return obj


def write_objects(db: Database, objs, empty=False, many=False, silent=False, cursor=False):
    if len(objs) == 0:
        return

    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    clazz = objs[0].__class__
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id));"

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
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id));"

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

def update_generator(db: Database, clazz, generator: Generator):
    cur = db.cursor()
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id));"

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

def get_element_name_with_ns(clazz):
    name = getattr(clazz.Meta, 'name', clazz.__name__)
    return "{" + clazz.Meta.namespace + "}" + name

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
    else:
        clean_element_names = [x[0] for x in entitiesinversion if not x[0].endswith('Frame')]
        interesting_element_names =  [get_element_name_with_ns(x[1]) for x in entitiesinversion if not x[0].endswith('Frame')]

    return clean_element_names, interesting_element_names

def setup_database(db: Database, classes, clean=False, cursor=False):
    if cursor:
        cur = db.cursor()
    else:
        cur = db.con

    clean_element_names, interesting_element_names = classes

    if clean:
        for objectname in clean_element_names:
            sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
            cur.execute(sql_drop_table)
        cur.execute("VACUUM;")

    sql_create_table = f"CREATE TABLE IF NOT EXISTS embedded (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, path TEXT NOT NULL, PRIMARY KEY (parent_class, parent_id, parent_version, class, id, version, ordr));"
    print(sql_create_table)
    cur.execute(sql_create_table)

    sql_create_table = f"CREATE TABLE IF NOT EXISTS referencing (parent_class varchar(64) NOT NULL, parent_id varchar(64) NOT NULL, parent_version varchar(64) not null, class varchar(64) not null, ref varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, PRIMARY KEY (parent_class, parent_id, parent_version, class, ref, version, ordr));"
    print(sql_create_table)
    cur.execute(sql_create_table)

    for objectname in clean_element_names:
        # TODO: optimize
        clazz = getattr(sys.modules['netex'], objectname)
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
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object {db.serializer.sql_type} NOT NULL, last_modified TIMESTAMP NOT NULL PRIMARY KEY (id));"

        print(sql_create_table)
        cur.execute(sql_create_table)

def get_local_name(element):
    if hasattr(element, 'Meta') and hasattr(element.Meta, 'name'):
        return element.Meta.name
    return element.__name__


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

    clean_element_names, interesting_element_names = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        objectname = clean_element_names[i]
        clazz = getattr(sys.modules['netex'], objectname)
        clazz_by_name[interesting_element_names[i]] = clazz

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

                # update_embedded_referencing(cur, object)
                current_element_tag = None


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
    clean_element_names, interesting_element_names = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        objectname = clean_element_names[i]
        clazz = getattr(sys.modules['netex'], objectname)
        clazz_by_name[interesting_element_names[i]] = clazz

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
                    cur.execute(sql_insert_object, (parent.__class__.__name__, parent.id, parent.version, obj.name_of_ref_class, obj.ref, obj.version or 'any', order))
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
    clean_element_names, interesting_element_names = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        objectname = clean_element_names[i]
        clazz = getattr(sys.modules['netex'], objectname)
        clazz_by_name[interesting_element_names[i]] = clazz

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
                            clazz.__name__, parent.id, parent.version, obj.__class__.__name__, obj.id, version, order))
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
                        cur.execute(sql_insert_object, (parent.__class__.__name__, parent.id, parent.version, obj.name_of_ref_class, obj.ref, obj.version or 'any', order))
                    except duckdb.duckdb.ConstraintException:
                        pass

                    if count == 1000:
                        cur.execute("CHECKPOINT;")
                        count = 0

                    count += 1

        cur.execute("CHECKPOINT;")


def attach_objects(con, read_database: str, clazz):
    type = getattr(clazz.Meta, 'name', clazz.__name__)
    # con.execute(f"DROP TABLE IF EXISTS {type};")
    # con.execute(f"CREATE VIEW {type} AS SELECT * FROM original.{type};")

    # Workaround for https://github.com/duckdb/duckdb-web/issues/3495
    attach_source(con, read_database)
    con.execute(f"INSERT INTO {type} SELECT * FROM original.{type};")

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

