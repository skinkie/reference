from dataclasses import dataclass
from netex.mobility_journey_frame_ref_structure import MobilityJourneyFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityJourneyFrameRef(MobilityJourneyFrameRefStructure):
    """
    Reference to a MOBILITY JOURNEY FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
