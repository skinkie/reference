from dataclasses import dataclass

from .parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingBay(ParkingBayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
