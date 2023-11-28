from dataclasses import dataclass
from netex.mobility_service_frame_ref_structure import MobilityServiceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceFrameRef(MobilityServiceFrameRefStructure):
    """
    Reference to a MOBILITY SERVICE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
