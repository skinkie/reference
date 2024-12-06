from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from netex import PublicationDelivery, CompositeFrame, SiteFrame

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
pd = parser.parse(Path("/tmp/smaller.xml"), PublicationDelivery)
composite_frame: CompositeFrame = pd.data_objects.choice[0]
site_frame: SiteFrame = composite_frame.frames.common_frame[1]

print("This works")
print(site_frame.stop_places.stop_place[0].accessibility_assessment.limitations.accessibility_limitation.wheelchair_access)

print("This fails")
try:
    print(site_frame.stop_places.stop_place[0].accessibility_assessment.limitations.accessibility_limitation)
except:
    print("Told you so...")
    raise

print("Therefore this fails too")
try:
    print(site_frame.stop_places.stop_place[0])
except:
    print("Told you so...")
    raise