from dataclasses import dataclass, field
from netex.vehicle_sharing_parking_bay_version_structure import VehicleSharingParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingBay(VehicleSharingParkingBayVersionStructure):
    """A spot in the PARKING AREA dedicated to vehicle sharing or rental.

    +v1.2.2

    :ivar id: Identifier of VEHICLE SHARING PARKING BAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
