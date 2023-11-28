from dataclasses import dataclass, field
from netex.addressable_place_version_structure import AddressablePlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AddressablePlace(AddressablePlaceVersionStructure):
    """
    A PLACE which may have an address.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
