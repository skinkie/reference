from dataclasses import dataclass
from netex.class_in_frame_structure import ClassInFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassInFrame(ClassInFrameStructure):
    """Class of an entity in a VERSION FRAME.

    This is a metaclass that allows services to specify whether a class
    must or must not be present.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
