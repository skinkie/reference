from io import BytesIO

import duckdb
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

ns_map = {None: 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

con = duckdb.connect(database='merge.duckdb')
with duckdb.cursor(con) as cur:
    with open('/tmp/test.xml', 'wb') as f:
        with lxml.etree.xmlfile(f) as xf:
            with xf.element('{http://www.netex.org.uk/netex}scheduledStopPoints', nsmap=ns_map):
                cur.execute("select xml from scheduledStopPoints;")
                df = cur.df()
                for xml in df.get('xml'):
                    element = lxml.etree.fromstring(xml)
                    xf.write(element)
                    xf.flush()
