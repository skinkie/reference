from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.parking_ref import ParkingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a PARKING.
    """
    class Meta:
        name = "parkingRefs_RelStructure"

    parking_ref: List[ParkingRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
