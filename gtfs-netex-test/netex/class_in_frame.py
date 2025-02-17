from dataclasses import dataclass

from .class_in_frame_structure import ClassInFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClassInFrame(ClassInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
