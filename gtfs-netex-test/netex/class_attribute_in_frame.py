from dataclasses import dataclass

from .class_attribute_in_frame_structure import ClassAttributeInFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClassAttributeInFrame(ClassAttributeInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
