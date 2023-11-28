from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReservedSpaceFacilityEnumeration(Enum):
    """
    Allowed values for Reserved Space Facility.
    """
    UNKNOWN = "unknown"
    LOUNGE = "lounge"
    HALL = "hall"
    MEETING_POINT = "meetingPoint"
    GROUP_POINT = "groupPoint"
    RECEPTION = "reception"
    SHELTER = "shelter"
    SEATS = "seats"
