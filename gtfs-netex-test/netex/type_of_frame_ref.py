from dataclasses import dataclass
from .type_of_frame_ref_structure import TypeOfFrameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFrameRef(TypeOfFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
