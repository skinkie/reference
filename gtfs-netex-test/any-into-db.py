import duckdb
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

empty_db = True

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

def generate_type(tree, type: str):
    for element in tree.iterfind(f".//{type}"):
        yield element.attrib['id'], lxml.etree.tostring(element, encoding='utf-8')

def load_type(cur, tree, xml_type: str, empty_db=False):
    type = xml_type.split('}')[-1]
    if empty_db:
        cur.execute(f"""DROP TABLE IF EXISTS {type};""")

    cur.execute(f"""CREATE TABLE IF NOT EXISTS {type} (id TEXT, xml TEXT);""")
    cur.executemany(f"""INSERT INTO {type} (id, xml) VALUES (?, ?)""", list(generate_type(tree, xml_type))) # TODO: check if we can avoid list()

def load(input_filename: str):
    con = duckdb.connect(database='netex.duckdb')
    with duckdb.cursor(con) as cur:
        tree = lxml.etree.parse(input_filename)
        load_type(cur, tree, '{http://www.netex.org.uk/netex}AvailabilityCondition', empty_db=True)

# load('/tmp/NeTEx_ARR_NL_20240430_20240501_1418.xml.gz')
# load('/tmp/NeTEx_DOVA_epiap_20240510013000.xml.gz')