from dataclasses import dataclass, field
from netex.road_address_version_structure import RoadAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadAddress(RoadAddressVersionStructure):
    """
    Specialisation of ADDRESS refining it by using the characteristics such as road
    number, and name used for conventional identification of along a road.

    :ivar id: Identifier of  ROAD ADDRESS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
