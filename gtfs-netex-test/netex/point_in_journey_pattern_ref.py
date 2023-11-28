from dataclasses import dataclass
from netex.point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointInJourneyPatternRef(PointInJourneyPatternRefStructure):
    """Reference to a POINT IN JOURNEY PATTERN.

    If Given by Context does not need to stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
