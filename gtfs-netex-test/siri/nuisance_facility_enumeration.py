from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class NuisanceFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    SMOKING = "smoking"
    NO_SMOKING = "noSmoking"
    MOBILE_PHONE_USE_ZONE = "mobilePhoneUseZone"
    MOBILE_PHONE_FREE_ZONE = "mobilePhoneFreeZone"
