from dataclasses import dataclass

from .mobility_journey_frame_ref_structure import MobilityJourneyFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MobilityJourneyFrameRef(MobilityJourneyFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
