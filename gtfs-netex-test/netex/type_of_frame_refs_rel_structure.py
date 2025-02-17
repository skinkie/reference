from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_frame_ref import TypeOfFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfFrameRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFrameRefs_RelStructure"

    type_of_frame_ref: list[TypeOfFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
