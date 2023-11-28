from dataclasses import dataclass, field
from netex.parking_capacity_versioned_child_structure import ParkingCapacityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingCapacity(ParkingCapacityVersionedChildStructure):
    """
    Capacity of a PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
