from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_place_ref import TypeOfPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPE OF PLACEs.
    """
    class Meta:
        name = "typeOfPlaceRefs_RelStructure"

    type_of_place_ref: List[TypeOfPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
