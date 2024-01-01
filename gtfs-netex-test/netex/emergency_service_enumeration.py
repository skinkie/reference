from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EmergencyServiceEnumeration(Enum):
    POLICE = "police"
    FIRE = "fire"
    FIRST_AID = "firstAid"
    SOS_POINT = "sosPoint"
    OTHER = "other"
