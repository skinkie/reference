from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RegisterBreakOfJourneyEnumeration(Enum):
    NONE = "none"
    MARK_BY_STAFF = "markByStaff"
    MARK_BY_VALIDATOR = "markByValidator"
    MARK_BY_MOBILE_APP = "markByMobileApp"
    OTHER = "other"
