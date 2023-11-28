from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_frame_ref import TypeOfFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFrameRefsRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more TYPEs OF VERSION FRAME.
    """
    class Meta:
        name = "typeOfFrameRefs_RelStructure"

    type_of_frame_ref: List[TypeOfFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
