from dataclasses import dataclass, field
from netex.stop_point_in_journey_pattern_versioned_child_structure import StopPointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPointInJourneyPattern(StopPointInJourneyPatternVersionedChildStructure):
    """The use of a SCHEDULED STOP POINT in a specified order.

    within a JOURNEY PATTERN or SERVICE PATTERN.

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
