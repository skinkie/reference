from dataclasses import dataclass
from netex.type_of_frame_ref_structure import TypeOfFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFrameRef(TypeOfFrameRefStructure):
    """
    Reference to a TYPE OF VERSION FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
