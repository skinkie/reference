from dataclasses import dataclass

from .timing_point_in_journey_pattern_versioned_child_structure import TimingPointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingPointInJourneyPattern(TimingPointInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
