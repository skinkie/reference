from dataclasses import dataclass
from .class_relationship_in_frame_structure import (
    ClassRelationshipInFrameStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassRelationshipInFrame(ClassRelationshipInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
