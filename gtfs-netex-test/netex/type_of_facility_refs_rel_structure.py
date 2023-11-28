from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFacilityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPE OF FACILITY.
    """
    class Meta:
        name = "typeOfFacilityRefs_RelStructure"

    type_of_facility_ref: List[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
