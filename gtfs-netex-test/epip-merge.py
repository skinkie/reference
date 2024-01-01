import glob
from typing import Set

import duckdb
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

frames = [".//{http://www.netex.org.uk/netex}ServiceFrame", ".//{http://www.netex.org.uk/netex}TimetableFrame",
          ".//{http://www.netex.org.uk/netex}ResourceFrame", ".//{http://www.netex.org.uk/netex}ServiceCalendar",
          ".//{http://www.netex.org.uk/netex}SiteFrame"]

elements = [".//{http://www.netex.org.uk/netex}codespaces"]

children = [".//{http://www.netex.org.uk/netex}CompositeFrame/{http://www.netex.org.uk/netex}FrameDefaults"]

ns_map = {'netex': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

aggregations: Set[str] = set([])

def aggregation_to_database(aggretation, aggregations: Set[str]):
    if aggregations is None:
        return

    aggretation_tag = aggretation.tag.split('}')[-1]

    if aggretation_tag[0] < 'a' or aggretation_tag[0] > 'z':
        return

    if aggretation_tag not in aggregations:
        cur.execute(f"DROP TABLE IF EXISTS {aggretation_tag};")
        cur.execute(f"CREATE TABLE {aggretation_tag} (id TEXT PRIMARY KEY, xml TEXT);")
        aggregations.add(aggretation_tag)

    values = [(child.attrib['id'], lxml.etree.tostring(child).decode('utf8'),) for child in aggretation]
    cur.executemany(f"INSERT INTO {aggretation_tag} VALUES (?, ?) ON CONFLICT DO NOTHING", values)

def child_to_database(element, aggregations: Set[str]):
    if element is None:
        return

    aggretation_tag = element.tag.split('}')[-1]

    if aggretation_tag not in aggregations:
        cur.execute(f"DROP TABLE IF EXISTS {aggretation_tag};")
        cur.execute(f"CREATE TABLE {aggretation_tag} (id TEXT PRIMARY KEY, xml TEXT);")
        aggregations.add(aggretation_tag)

    values = [(element.getparent().attrib['id'], lxml.etree.tostring(element).decode('utf8'),)]
    cur.executemany(f"INSERT INTO {aggretation_tag} VALUES (?, ?) ON CONFLICT DO NOTHING", values)


con = duckdb.connect(database='merge.duckdb')
with duckdb.cursor(con) as cur:
    parser = lxml.etree.XMLParser(remove_blank_text=True, ns_clean=True)

    for input_filename in glob.glob("netex-output-epip/Flix_*.xml"):
        tree = lxml.etree.parse(input_filename, parser=parser)
        for frame_element in frames:
            frame = tree.find(frame_element)
            for aggretation in frame[:]:
                aggregation_to_database(aggretation, aggregations)

        for element in elements:
            aggretation = tree.find(element)
            aggregation_to_database(aggretation, aggregations)

        for child in children:
            child = tree.find(child)
            child_to_database(child, aggregations)
