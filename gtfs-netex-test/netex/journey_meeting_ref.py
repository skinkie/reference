from dataclasses import dataclass
from netex.journey_meeting_ref_structure import JourneyMeetingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyMeetingRef(JourneyMeetingRefStructure):
    """
    Reference to a JOURNEY MEETING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
