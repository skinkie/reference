from dataclasses import dataclass, field
from netex.point_in_journey_pattern_versioned_child_structure import PointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointInJourneyPattern(PointInJourneyPatternVersionedChildStructure):
    """
    A STOP POINT or TIMING POINT in a JOURNEY PATTERN with its order in that
    JOURNEY PATTERN.

    :ivar id:
    :ivar order: Order of POINT in sequence.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
