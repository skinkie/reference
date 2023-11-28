from dataclasses import dataclass
from netex.vehicle_sharing_parking_area_ref_structure import VehicleSharingParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingAreaRef(VehicleSharingParkingAreaRefStructure):
    """Reference to a VEHICLE SHARING PARKING AREA.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
