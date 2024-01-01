from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NuisanceFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    SMOKING = "smoking"
    NO_SMOKING = "noSmoking"
    FAMILY_AREA = "familyArea"
    CHILDFREE_AREA = "childfreeArea"
    ANIMALS_ALLOWED = "animalsAllowed"
    NO_ANIMALS = "noAnimals"
    BREASTFEEDING_FRIENDLY = "breastfeedingFriendly"
    MOBILE_PHONE_USE_ZONE = "mobilePhoneUseZone"
    MOBILE_PHONE_FREE_ZONE = "mobilePhoneFreeZone"
