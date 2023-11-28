from dataclasses import dataclass, field
from netex.vehicle_pooling_parking_bay_version_structure import VehiclePoolingParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingBay(VehiclePoolingParkingBayVersionStructure):
    """A dedicated space of a PARKING AREA for either vehicles active in a pooling
    service or vehicles of a pooling service users  where vehicles are left for a
    longer time.

    +v1.2.2

    :ivar id: Identifier of VEHICLE POOLING PARKING BAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
