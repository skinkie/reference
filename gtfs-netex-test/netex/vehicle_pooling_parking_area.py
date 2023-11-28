from dataclasses import dataclass, field
from netex.vehicle_pooling_parking_area_version_structure import VehiclePoolingParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingArea(VehiclePoolingParkingAreaVersionStructure):
    """A dedicated space of a PARKING AREA for either vehicles active in a pooling
    service or  vehicles of a pooling service users  where vehicles are left for a
    longer time.

    +v1.2.2

    :ivar id: Identifier of VEHICLE POOLING PARKING AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
