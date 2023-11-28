from dataclasses import dataclass, field
from netex.place_in_sequence_versioned_child_structure import PlaceInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceInSequence(PlaceInSequenceVersionedChildStructure):
    """Point traversed by a NAVIGATION PATH in sequence.

    Maybe a PLACE PATH JUNCTION or POINT.

    :ivar id: Identifier of ENTITY.
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
