from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from netex import StopPointInJourneyPattern, TimingLinkRefStructure, TimingLinkRef

spijp = StopPointInJourneyPattern(onward_timing_link_ref=TimingLinkRefStructure(ref="test")) # This is based on type hinting in PyCharm.
spijp1 = StopPointInJourneyPattern(onward_timing_link_ref=TimingLinkRef(ref="test")) # This is based on type hinting in PyCharm.

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

print(serializer.render(spijp, ns_map))

print(serializer.render(spijp1, ns_map))
