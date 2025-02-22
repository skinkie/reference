from dataclasses import dataclass

from .journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternRef(JourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
