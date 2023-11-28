from dataclasses import dataclass
from netex.parking_bay_ref_structure import ParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingBayRefStructure(ParkingBayRefStructure):
    """
    Type for a reference to a VEHICLE SHARING PARKING BAY.
    """
