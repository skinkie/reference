from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleVehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of PERSONAL TRANSPORT TYPEs.
    """
    class Meta:
        name = "simpleVehicleTypeRefs_RelStructure"

    simple_vehicle_type_ref: List[SimpleVehicleTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "SimpleVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
