from dataclasses import dataclass
from netex.parking_capacity_ref_structure import ParkingCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingCapacityRef(ParkingCapacityRefStructure):
    """
    Reference to a PARKING CAPACITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
