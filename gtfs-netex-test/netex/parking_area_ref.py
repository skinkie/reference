from dataclasses import dataclass
from netex.parking_area_ref_structure import ParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingAreaRef(ParkingAreaRefStructure):
    """
    Reference to a PARKING AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
