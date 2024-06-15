from typing import T, List, Generator

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

def load_local(con, clazz: T, limit=None) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    try:
        if limit is not None:
            cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {type};")
    except:
        return []

    objs: List[T] = []
    for xml, in cur.fetchall():
        if isinstance(xml, str):
            obj = parser.from_string(xml, clazz)
        else:
            obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs

def load_generator(con, clazz, limit=None):
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
        if isinstance(xml[0], str):
            yield parser.from_string(xml[0], clazz)
        else:
            yield parser.from_bytes(xml[0], clazz)

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

def write_lxml_generator(con, clazz, generator: Generator):
    cur = con.cursor()
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], obj.attrib['version'], obj.attrib['order'], etree.tostring(obj)
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], obj.attrib['version'], etree.tostring(obj)
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.attrib['id'], etree.tostring(obj)
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object) VALUES (?, ?, ?);', _prepare3(generator, objectname))
    else:
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object) VALUES (?, ?);', _prepare2(generator, objectname))

    print('\n')

def get_single(con, clazz: T, id, version) -> T:
    type = getattr(clazz.Meta, 'name', clazz.__name__)
    cur = con.cursor()
    if version == 'any' or version is None:
        cur.execute(f"SELECT object FROM {type} WHERE id = ? ORDER BY version DESC LIMIT 1;", (id,))
    else:
        cur.execute(f"SELECT object FROM {type} WHERE id = ? AND version = ? LIMIT 1;", (id, version,))

    row = cur.fetchone()
    if row is not None:
        if isinstance(row[0], str):
            obj = parser.from_string(row[0], clazz)
        else:
            obj = parser.from_bytes(row[0], clazz)

        return obj


def write_objects(con, objs, empty=False, many=False):
    if len(objs) == 0:
        return

    cur = con.cursor()
    clazz = objs[0].__class__
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    if many:
        print(objectname, len(objs))
        if hasattr(clazz, 'order'):
            cur.executemany(f'INSERT INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', [(obj.id, obj.version, obj.order, serializer.render(obj, ns_map).replace('\n', '')) for obj in objs])
        elif hasattr(clazz, 'version'):
            cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', [(obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '')) for obj in objs])
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);',
                            [(obj.id, serializer.render(obj, ns_map).replace('\n', '')) for obj in objs])
    else:
        for i in range(0, len(objs)):
            obj = objs[i]
            if hasattr(clazz, 'order'):
                cur.execute(f'INSERT INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', (obj.id, obj.version, obj.order, serializer.render(obj, ns_map).replace('\n', '')))
            elif hasattr(clazz, 'version'):
                cur.execute(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', (obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '')))
            else:
                cur.execute(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);', (obj.id, serializer.render(obj, ns_map).replace('\n', '')))

            if i % 13 == 0:
                print('\r', objectname, str(i), end = '')
        print('\r', objectname, len(objs), end='')


def write_generator(con, clazz, generator: Generator, empty=False):
    cur = con.cursor()
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, obj.order, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare4(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare3(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object) VALUES (?, ?, ?);', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', _prepare3(generator, objectname))
    else:
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare2(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object) VALUES (?, ?);', a)
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);', _prepare2(generator, objectname))

    print('\n')

def update_generator(con, clazz, generator: Generator):
    cur = con.cursor()
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if hasattr(clazz, 'order'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version, ordr));"
    elif hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, obj.order, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, serializer.render(obj, ns_map).replace('\n', '')
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare4(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare3(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object) VALUES (?, ?, ?);', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, version, object) VALUES (?, ?, ?);', _prepare3(generator, objectname))
    else:
        if con.__class__.__name__ == 'DuckDBPyConnection':
            for a in _prepare2(generator, objectname):
                cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object) VALUES (?, ?);', a)
        else:
            cur.executemany(f'INSERT OR REPLACE INTO {objectname} (id, object) VALUES (?, ?);', _prepare2(generator, objectname))

    print('\n')