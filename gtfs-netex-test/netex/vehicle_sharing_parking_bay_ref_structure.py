from dataclasses import dataclass

from .parking_bay_ref_structure import ParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingParkingBayRefStructure(ParkingBayRefStructure):
    pass
