from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EmergencyServiceEnumeration(Enum):
    """
    Allowed values for Emergency Service Facility.
    """
    POLICE = "police"
    FIRE = "fire"
    FIRST_AID = "firstAid"
    SOS_POINT = "sosPoint"
    OTHER = "other"
