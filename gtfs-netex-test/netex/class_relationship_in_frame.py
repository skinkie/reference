from dataclasses import dataclass
from netex.class_relationship_in_frame_structure import ClassRelationshipInFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassRelationshipInFrame(ClassRelationshipInFrameStructure):
    """Relationship of Class of ENTITY.

    This is a metaclass that allows services to specify whether a
    Relationship must or must not be present for a class in a given
    frame.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
