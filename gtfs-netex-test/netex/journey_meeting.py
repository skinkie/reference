from dataclasses import dataclass, field
from netex.journey_meeting_version_structure import JourneyMeetingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyMeeting(JourneyMeetingVersionStructure):
    """
    A time constraint for one or several SERVICE JOURNEYs fixing interchanges
    between them and/or an external event (e.g. arrival or departure of a feeder
    line, opening time of the theatre, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
