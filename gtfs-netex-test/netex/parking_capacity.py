from dataclasses import dataclass
from .parking_capacity_versioned_child_structure import (
    ParkingCapacityVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacity(ParkingCapacityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
