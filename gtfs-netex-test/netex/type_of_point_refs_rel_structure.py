from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_point_ref import TypeOfPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfPointRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfPointRefs_RelStructure"

    type_of_point_ref: list[TypeOfPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
