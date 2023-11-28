from dataclasses import dataclass, field
from typing import List
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfDistanceMatrixElementsRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of GROUP OF DISTANCE MATRIX ELEMENTss.
    """
    class Meta:
        name = "groupOfDistanceMatrixElementsRefs_RelStructure"

    group_of_distance_matrix_elements_ref: List[GroupOfDistanceMatrixElementsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
