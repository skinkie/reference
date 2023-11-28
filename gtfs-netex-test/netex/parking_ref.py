from dataclasses import dataclass
from netex.parking_ref_structure import ParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingRef(ParkingRefStructure):
    """
    Reference to a PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
