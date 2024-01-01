from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceFacilityEnumeration(Enum):
    PERSONAL_ASSISTANCE = "personalAssistance"
    BOARDING_ASSISTANCE = "boardingAssistance"
    WHEELCHAIR_ASSISTANCE = "wheelchairAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    WHEELCHAIR_USE = "wheelchairUse"
    CONDUCTOR = "conductor"
    INFORMATION = "information"
    OTHER = "other"
    NONE = "none"
    ANY = "any"
