from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingPointEnumeration(Enum):
    MEETING_POINT = "meetingPoint"
    GROUP_MEETING = "groupMeeting"
    SCHOOL_MEETING_POINT = "schoolMeetingPoint"
    OTHER = "other"
