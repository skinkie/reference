from dataclasses import dataclass
from netex.timing_point_in_journey_pattern_ref_structure import TimingPointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointInJourneyPatternRef(TimingPointInJourneyPatternRefStructure):
    """Reference to a TIMING POINT IN JOURNEY PATTERN.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
