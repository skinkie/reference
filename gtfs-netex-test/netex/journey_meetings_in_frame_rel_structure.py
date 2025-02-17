from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_meeting import JourneyMeeting

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyMeetingsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyMeetingsInFrame_RelStructure"

    journey_meeting: list[JourneyMeeting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeeting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
