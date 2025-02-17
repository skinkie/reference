from dataclasses import dataclass

from .type_of_frame_ref_structure import TypeOfFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfFrameRef(TypeOfFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
