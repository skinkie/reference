from dataclasses import dataclass
from netex.general_frame_ref_structure import GeneralFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralFrameRef(GeneralFrameRefStructure):
    """
    Reference to a GENERAL FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
