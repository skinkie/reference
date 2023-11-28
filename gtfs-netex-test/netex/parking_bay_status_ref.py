from dataclasses import dataclass
from netex.parking_bay_status_ref_structure import ParkingBayStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayStatusRef(ParkingBayStatusRefStructure):
    """Reference to a PARKING BAY STATUS.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
