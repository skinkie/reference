from dataclasses import dataclass, field

from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfDistanceMatrixElementsRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfDistanceMatrixElementsRefs_RelStructure"

    group_of_distance_matrix_elements_ref: list[GroupOfDistanceMatrixElementsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
