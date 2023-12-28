import glob
from typing import Set

import duckdb
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

frames = [".//{http://www.netex.org.uk/netex}ServiceFrame", ".//{http://www.netex.org.uk/netex}TimetableFrame",
          ".//{http://www.netex.org.uk/netex}ResourceFrame", ".//{http://www.netex.org.uk/netex}ServiceCalendar",
          ".//{http://www.netex.org.uk/netex}SiteFrame"]

ns_map = {'netex': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

aggregations: Set[str] = set([])

con = duckdb.connect(database='merge.duckdb')
with duckdb.cursor(con) as cur:
    parser = lxml.etree.XMLParser(remove_blank_text=True, ns_clean=True)

    for input_filename in glob.glob("netex-output-epip/Flix_*.xml"):
        tree = lxml.etree.parse(input_filename, parser=parser)
        for frame_element in frames:
            frame = tree.find(frame_element)
            for aggretation in frame[:]:
                aggretation_tag = aggretation.tag.split('}')[-1]

                if aggretation_tag[0] < 'a' or aggretation_tag[0] > 'z':
                    continue

                if aggretation_tag not in aggregations:
                    cur.execute(f"DROP TABLE IF EXISTS {aggretation_tag};")
                    cur.execute(f"CREATE TABLE {aggretation_tag} (id TEXT PRIMARY KEY, xml TEXT);")
                    aggregations.add(aggretation_tag)

                values = [(child.attrib['id'], lxml.etree.tostring(child).decode('utf8'),) for child in aggretation]
                cur.executemany(f"INSERT INTO {aggretation_tag} VALUES (?, ?) ON CONFLICT DO NOTHING", values)