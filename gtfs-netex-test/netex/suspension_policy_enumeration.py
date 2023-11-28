from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SuspensionPolicyEnumeration(Enum):
    """
    Allowed values for Suspension Policy.

    :cvar NONE: Suspension not allowed.
    :cvar FOR_CERTIFIED_ILLNESS: Suspension allowed for illness.
    :cvar FOR_PARENTAL_LEAVE: Suspension allowed  for parental leave.
    :cvar FOR_HOLIDAY: Suspension allowed  for holiday.
    :cvar FOR_ANY_REASON: Suspension allowed  for any reason.
    """
    NONE = "none"
    FOR_CERTIFIED_ILLNESS = "forCertifiedIllness"
    FOR_PARENTAL_LEAVE = "forParentalLeave"
    FOR_HOLIDAY = "forHoliday"
    FOR_ANY_REASON = "forAnyReason"
