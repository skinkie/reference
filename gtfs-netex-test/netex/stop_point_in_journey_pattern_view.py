from dataclasses import dataclass
from netex.stop_point_in_journey_pattern_derived_view_structure import StopPointInJourneyPatternDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPointInJourneyPatternView(StopPointInJourneyPatternDerivedViewStructure):
    """Simplified STOP POINT IN JOURNEY PATTERN.

    Assumes single time demand.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
