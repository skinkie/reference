from dataclasses import dataclass, field
from netex.fare_point_in_pattern_versioned_child_structure import FarePointInPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePointInPattern(FarePointInPatternVersionedChildStructure):
    """
    A POINT IN PATTERN which represents the start or end of a FARE SECTION.

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
