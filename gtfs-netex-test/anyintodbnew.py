from isal import igzip_threaded
import sqlite3
from lxml import etree
import sys

from netex import JourneyPart


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
        clean_element_names = sorted([x[0] for x in entitiesinversion if x[0] in filter])
        interesting_element_names =  set([get_element_name_with_ns(x[1]) for x in entitiesinversion if x[0] in filter])
    else:
        clean_element_names = sorted([x[0] for x in entitiesinversion if not x[0].endswith('Frame')])
        interesting_element_names =  set([get_element_name_with_ns(x[1]) for x in entitiesinversion if not x[0].endswith('Frame')])

    return clean_element_names, interesting_element_names

def setup_database(con, classes, clean=False):
    cur = con.cursor()
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

        if hasattr(clazz, 'order'):
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, ordr integer, object text NOT NULL, PRIMARY KEY (id, version, ordr));"

        elif hasattr(clazz, 'version'):
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"

        else:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL PRIMARY KEY (id));"

        print(sql_create_table)
        cur.execute(sql_create_table)



def insert_database(con, classes, f=None):
    if f is None:
        return

    cur = con.cursor()
    clean_element_names, interesting_element_names = classes
    events = ("start", "end")
    context = etree.iterparse(f, events=events, remove_blank_text=True)
    current_element = None
    for event, element in context:
        if event == 'end' and element.tag in interesting_element_names: # https://stackoverflow.com/questions/65935392/why-does-elementtree-iterparse-sometimes-retrieve-xml-elements-incompletely
            # current_element = element.tag
            xml = etree.tostring(element)
            if 'id' not in element.attrib:
                # print(xml)
                continue

            id = element.attrib['id']
            version = element.attrib.get('version', None)
            order = element.attrib.get('order', None)

            localname = element.tag.split('}')[-1] # localname
            if order is not None:
                sql_insert_object = f"""INSERT INTO {localname} (id, version, ordr, object) VALUES (?, ?, ?, ?);"""
                try:
                    cur.execute(sql_insert_object, (id, version, order, xml,))
                except:
                    print(xml)
                    pass

            elif version is not None:
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
            yield zip.open(zipfilename)

if __name__ == "__main__":
    filenames = ['/home/netex/NeTEx_ARR_NL_20240516_20240517_1418.xml.gz', '/home/netex/NeTEx_DOVA_epiap_20240517013000.xml.gz']

    classes = get_interesting_classes()

    with sqlite3.connect("/tmp/netex.sqlite") as con:
        if True:
            setup_database(con, classes, True)

        for filename in filenames:
            for sub_file in open_netex_file(filename):
                insert_database(con, classes, sub_file)

"""
Er zijn twee echte todo's:
 1. NeTEx heeft frame defaults, dus je wilt die framedefaults eigenlijk "denormaliseren" over de objecten die er onder hangen. Dat geldt ook voor dingen als 'versie' ligt een object onder een ander object dan mag je er vanuit gaan dat deze dezelfde versie heeft.
 2. De referenties die NeTEx maakt, die verwijzen naar een 'object', maar op een bepaalde manier ook naar een 'objecttype'. Als je naar een ander object type verwijst verwijs je naar een "nameOfRefClass". Je zou dat soort dingen ook wil voorbewerken, dus er vanuit gaan dat je weet naar welk object wijst.

Qua architectuur is een lastige de volgende:
 1. NoticeAssignment kan technisch gezien op elk embedded object werken, denk aan een Call, PassingTime of StopPointInJourneyPattern. Als je objecten individueel in de database hangt, zonder die embedding in losse tabellen te knallen, kun je geen explicite verwijzing maken zonder eerst te verwijzen naar het bovenliggende object.
,6 min,
Ik wil nog eens nadenken of ik technisch gezien iets kan doen dat ik embeddings zelf ook in losse object tabellen kan hangen, en dan iets doen met een terugverwijzing naar het hoofdobject waar het onderhangt.
,5 min,
Dan heb je eigenlijk "alles" wat je wilt.
"""