import sys
from typing import T, List, Generator

from isal import igzip_threaded
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from mro_attributes import list_attributes

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)
serializer.encoding = 'utf-8'

def load_local(con, clazz: T, limit=None, filter=None, cursor=False) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    if cursor:
        cur = con.cursor()
    else:
        cur = con

    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
        elif limit is not None:
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

def load_generator(con, clazz, limit=None, filter=None):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    try:
        if filter is not None:
            cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
        elif limit is not None:
            cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
        else:
            cur.execute(f"SELECT object FROM {type};")
    except:
        return

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
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
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
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, version, object) VALUES (?, ?, ?);', _prepare3(generator, objectname))
    else:
        cur.execute(f'INSERT OR REPLACE INTO {objectname} (id, object) VALUES (?, ?);', _prepare2(generator, objectname))

    print('\n')

def get_single(con, clazz: T, id, version=None, cursor=False) -> T:
    if cursor:
        cur = con.cursor()
    else:
        cur = con

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
        if isinstance(row[0], str):
            obj = parser.from_string(row[0], clazz)
        else:
            obj = parser.from_bytes(row[0], clazz)

        return obj


def write_objects(con, objs, empty=False, many=False, silent=False, cursor=False):
    if len(objs) == 0:
        return

    if cursor:
        cur = con.cursor()
    else:
        cur = con

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

    try:
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

                if not silent:
                    if i % 13 == 0:
                        print('\r', objectname, str(i), end = '')
        if not silent:
            print('\r', objectname, len(objs), end='')
    except:
        raise
        # pass


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

def setup_database(con, classes, clean=False, cursor=False):
    if cursor:
        cur = con.cursor()
    else:
        cur = con

    clean_element_names, interesting_element_names = classes

    if clean:
        # SQLITE
        # cur.execute("PRAGMA writable_schema = 1;")
        # cur.execute("DELETE FROM sqlite_master WHERE type IN ('table', 'index', 'trigger');")
        # cur.execute("PRAGMA writable_schema = 0;")
        # con.commit()

        # DuckDB
        for objectname in clean_element_names:
            sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
            cur.execute(sql_drop_table)
        cur.execute("VACUUM;")

    for objectname in clean_element_names:
        # TODO: optimize
        clazz = getattr(sys.modules['netex'], objectname)
        optionals = {x[0]: x[1][1] for x in list_attributes(clazz) if x[0] in ('order', 'version')}
        ordr_opt = optionals.get('order', False)
        version_opt = optionals.get('version', False)

        if hasattr(clazz, 'order'):
            if ordr_opt:
                sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version));"
            else:
                sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer NOT NULL, object text NOT NULL, PRIMARY KEY (id, version, ordr));"

        elif hasattr(clazz, 'version'):
            if version_opt:
                sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64), object text NOT NULL, PRIMARY KEY (id));"
            else:
                sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"

        else:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL PRIMARY KEY (id));"

        print(sql_create_table)
        cur.execute(sql_create_table)

def insert_database(con, classes, f=None, cursor=False):
    if f is None:
        return

    if cursor:
        cur = con.cursor()
    else:
        cur = con

    clean_element_names, interesting_element_names = classes
    clazz_by_name = {}

    for i in range(0, len(interesting_element_names)):
        objectname = clean_element_names[i]
        clazz = getattr(sys.modules['netex'], objectname)
        clazz_by_name[interesting_element_names[i]] = clazz

    events = ("start", "end")
    context = etree.iterparse(f, events=events, remove_blank_text=True)
    current_element = None
    for event, element in context:
        if event == 'end' and element.tag in interesting_element_names: # https://stackoverflow.com/questions/65935392/why-does-elementtree-iterparse-sometimes-retrieve-xml-elements-incompletely
            # current_element = element.tag
            xml = etree.tostring(element, encoding='unicode')
            if 'id' not in element.attrib:
                # print(xml)
                continue

            clazz = clazz_by_name[element.tag]

            id = element.attrib['id']
            localname = element.tag.split('}')[-1] # localname

            if hasattr(clazz, 'order'):
                version = element.attrib.get('version', None)
                order = element.attrib.get('order', None)

                sql_insert_object = f"""INSERT INTO {localname} (id, version, ordr, object) VALUES (?, ?, ?, ?);"""
                try:
                    cur.execute(sql_insert_object, (id, version, order, xml,))
                except:
                    print(xml)
                    raise
                    pass

            elif hasattr(clazz, 'version'):
                version = element.attrib.get('version', None)

                sql_insert_object = f"""INSERT INTO {localname} (id, version, object) VALUES (?, ?, ?);"""
                try:
                    cur.execute(sql_insert_object, (id, version, xml,))
                except:
                    if localname == 'ServiceJourney':
                        print(xml)
                        raise

                    pass

            else:
                sql_insert_object = f"""INSERT INTO {localname} (id, object) VALUES (?, ?);"""
                try:
                    cur.execute(sql_insert_object, (id, xml,))
                except:
                    print(xml)
                    raise
                    pass


        # elif event == 'end' and element.tag == current_element:
        #    current_element = None


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
