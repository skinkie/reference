from dataclasses import dataclass, field
from netex.accommodation_versioned_child_structure import AccommodationVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Accommodation(AccommodationVersionedChildStructure):
    """
    Allowed combinations of accommodation.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
