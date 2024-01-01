from dataclasses import dataclass
from .parking_area_version_structure import ParkingAreaVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingAreaVersionStructure(ParkingAreaVersionStructure):
    class Meta:
        name = "VehiclePoolingParkingArea_VersionStructure"
