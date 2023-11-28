from dataclasses import dataclass
from netex.vehicle_sharing_parking_bay_ref_structure import VehicleSharingParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingBayRef(VehicleSharingParkingBayRefStructure):
    """Reference to a VEHICLE SHARING PARKING BAY.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
