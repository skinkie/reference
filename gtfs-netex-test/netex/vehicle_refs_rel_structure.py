from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLEs.
    """
    class Meta:
        name = "vehicleRefs_RelStructure"

    vehicle_ref: List[VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
