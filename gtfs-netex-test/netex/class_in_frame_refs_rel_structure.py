from dataclasses import dataclass, field
from typing import List

from .class_in_frame_ref import ClassInFrameRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassInFrameRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "ClassInFrameRefs_RelStructure"

    class_in_frame_ref: List[ClassInFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassInFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
