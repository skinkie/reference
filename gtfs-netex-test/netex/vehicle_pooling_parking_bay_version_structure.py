from dataclasses import dataclass
from .parking_bay_version_structure import ParkingBayVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingBayVersionStructure(ParkingBayVersionStructure):
    class Meta:
        name = "VehiclePoolingParkingBay_VersionStructure"
