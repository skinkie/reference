from dataclasses import dataclass

from .journey_pattern_headway_versioned_child_structure import JourneyPatternHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternHeadway(JourneyPatternHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
