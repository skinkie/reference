from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

from netex import Block, ServiceJourney, ServiceJourneyRef


def get_block(tree, quayref):
    found = tree.find(".//{http://www.netex.org.uk/netex}Quay[@id='" + quayref + "']")
    if found is not None:
        stop_place: StopPlace = parser.parse(found.getparent().getparent(), StopPlace)
        return stop_place
    else:
        print(f"Missing {quayref}")

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

b = []
d = dict()

tree = lxml.etree.parse("/tmp/NeTEx_ARR_NL_20240825_20240826_1419.xml.gz")
for block in tree.iterfind(".//{http://www.netex.org.uk/netex}Block"):
    block: Block = parser.parse(block, Block)
    for journey in block.journeys.choice:
        if isinstance(journey, ServiceJourneyRef):
            l = d.get(journey.ref, [])
            l.append(block.id)
            d[journey.ref] = l

    b.append(block)

# with open('/tmp/list.csv', 'w') as f:
#     for journey, blocks in d.items():
#         f.write(','.join([journey, str(len(blocks))]) + '\n')

with open('/tmp/sj-blockref.csv', 'w') as f:
    for block in b:
        for journey in reversed(block.journeys.choice):
            if isinstance(journey, ServiceJourneyRef):
                if len(d[journey.ref]) > 1:
                    break
                else:
                    f.write(','.join([journey.ref, block.id]) + '\n')