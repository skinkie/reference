from dataclasses import dataclass, field
from netex.parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GaragePoint(ParkingPointVersionStructure):
    """
    A subtype of PARKING POINT located in a GARAGE.

    :ivar id: Identifier of  GARAGE POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
