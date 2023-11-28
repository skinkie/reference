from dataclasses import dataclass, field
from typing import List
from netex.journey_meeting_ref import JourneyMeetingRef
from netex.journey_meeting_view import JourneyMeetingView
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyMeetingViewsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  JOURNEY MEETING VIEWs.
    """
    class Meta:
        name = "journeyMeetingViews_RelStructure"

    journey_meeting_ref_or_journey_meeting_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyMeetingRef",
                    "type": JourneyMeetingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeetingView",
                    "type": JourneyMeetingView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
