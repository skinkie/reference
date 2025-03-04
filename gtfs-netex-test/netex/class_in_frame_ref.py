from dataclasses import dataclass

from .class_in_frame_ref_structure import ClassInFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClassInFrameRef(ClassInFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
