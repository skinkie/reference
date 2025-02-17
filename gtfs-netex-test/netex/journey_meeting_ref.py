from dataclasses import dataclass

from .journey_meeting_ref_structure import JourneyMeetingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyMeetingRef(JourneyMeetingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
