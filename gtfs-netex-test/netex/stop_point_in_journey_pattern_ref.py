from dataclasses import dataclass
from netex.stop_point_in_journey_pattern_ref_structure import StopPointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPointInJourneyPatternRef(StopPointInJourneyPatternRefStructure):
    """Reference to a STOP POINT IN SEQUENCE.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
