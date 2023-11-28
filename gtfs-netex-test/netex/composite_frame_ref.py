from dataclasses import dataclass
from netex.composite_frame_ref_structure import CompositeFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompositeFrameRef(CompositeFrameRefStructure):
    """
    Reference to a COMPOSITE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
