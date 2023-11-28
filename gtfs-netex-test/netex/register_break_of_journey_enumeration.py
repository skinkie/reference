from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RegisterBreakOfJourneyEnumeration(Enum):
    """
    Allowed values for Register Break of Journey.

    :cvar NONE: No action needed.
    :cvar MARK_BY_STAFF: JourneyBreak must be marked by operator staff.
    :cvar MARK_BY_VALIDATOR: Journey Break must be marked by validator.
    :cvar MARK_BY_MOBILE_APP: Journey Break must be marked using mobile
        application.
    :cvar OTHER: Journey Break must be marked by othermeans.
    """
    NONE = "none"
    MARK_BY_STAFF = "markByStaff"
    MARK_BY_VALIDATOR = "markByValidator"
    MARK_BY_MOBILE_APP = "markByMobileApp"
    OTHER = "other"
