from dataclasses import dataclass

from .parking_capacity_versioned_child_structure import ParkingCapacityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingCapacity(ParkingCapacityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
