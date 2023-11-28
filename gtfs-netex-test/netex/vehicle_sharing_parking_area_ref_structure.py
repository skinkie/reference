from dataclasses import dataclass
from netex.parking_area_ref_structure import ParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingAreaRefStructure(ParkingAreaRefStructure):
    """
    Type for a reference to a VEHICLE SHARING PARKING AREA.
    """
