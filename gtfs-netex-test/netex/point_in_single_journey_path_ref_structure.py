from dataclasses import dataclass
from netex.point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointInSingleJourneyPathRefStructure(PointInJourneyPatternRefStructure):
    """
    Type for a reference to a POINT IN SINGLE JOURNEY PATH.
    """
