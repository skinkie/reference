from dataclasses import dataclass, field
from typing import Optional
from netex.place_version_structure import PlaceVersionStructure
from netex.postal_address import PostalAddress
from netex.road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AddressablePlaceVersionStructure(PlaceVersionStructure):
    """
    Type for an ADDRESSABLE PLACE.

    :ivar url: Default URL for ADDRESSABLE PLACE.
    :ivar image: Default image for ADDRESSABLE PLACE.
    :ivar postal_address:
    :ivar road_address: ADDRESS of a numbered building on a named road.
    """
    class Meta:
        name = "AddressablePlace_VersionStructure"

    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address: Optional[RoadAddress] = field(
        default=None,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
