from dataclasses import dataclass, field
from netex.vehicle_sharing_parking_area_version_structure import VehicleSharingParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingArea(VehicleSharingParkingAreaVersionStructure):
    """A dedicated part of the PARKING AREA for vehicle sharing or rental which is
    composed of one or more VEHICLE SHARING PARKING BAYs.

    +v1.2.2

    :ivar id: Identifier of VEHICLE SHARING PARKING AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
