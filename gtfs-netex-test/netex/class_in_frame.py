from dataclasses import dataclass
from .class_in_frame_structure import ClassInFrameStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassInFrame(ClassInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
