from dataclasses import dataclass
from netex.parking_bay_status_ref_structure import ParkingBayStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayConditionRef(ParkingBayStatusRefStructure):
    """Reference to a PARKING BAY CONDITION.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
