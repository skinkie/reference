from dataclasses import dataclass, field
from netex.timing_point_in_journey_pattern_versioned_child_structure import TimingPointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointInJourneyPattern(TimingPointInJourneyPatternVersionedChildStructure):
    """
    A NODE in a JOURNEY PATTERN which is a TIMING POINT.

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
