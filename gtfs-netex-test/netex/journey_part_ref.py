from dataclasses import dataclass

from .journey_part_ref_structure import JourneyPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPartRef(JourneyPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
