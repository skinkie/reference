from dataclasses import dataclass

from .point_in_journey_pattern_versioned_child_structure import PointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointInJourneyPattern(PointInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
