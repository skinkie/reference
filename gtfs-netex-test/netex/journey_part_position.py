from dataclasses import dataclass, field
from netex.journey_part_position_versioned_child_structure import JourneyPartPositionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartPosition(JourneyPartPositionVersionedChildStructure):
    """Position in train of JOURNEY PART from a given stop.

    +v1.1.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
