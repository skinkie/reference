from dataclasses import dataclass, field
from typing import List
from netex.class_in_frame import ClassInFrame
from netex.class_in_frame_ref import ClassInFrameRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassesInRepositoryRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of Classe Filter referencess.
    """
    class Meta:
        name = "classesInRepository_RelStructure"

    class_in_frame_ref_or_class_in_frame: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ClassInFrameRef",
                    "type": ClassInFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassInFrame",
                    "type": ClassInFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
