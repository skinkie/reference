from dataclasses import dataclass

from .parking_area_ref_structure import ParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingAreaRefStructure(ParkingAreaRefStructure):
    pass
