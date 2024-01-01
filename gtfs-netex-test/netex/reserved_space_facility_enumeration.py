from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReservedSpaceFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    LOUNGE = "lounge"
    HALL = "hall"
    MEETING_POINT = "meetingPoint"
    GROUP_POINT = "groupPoint"
    RECEPTION = "reception"
    SHELTER = "shelter"
    SEATS = "seats"
