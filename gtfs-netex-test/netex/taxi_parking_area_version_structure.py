from dataclasses import dataclass
from netex.parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiParkingAreaVersionStructure(ParkingAreaVersionStructure):
    """
    Type for TAXI PARKING AREA.
    """
    class Meta:
        name = "TaxiParkingArea_VersionStructure"
