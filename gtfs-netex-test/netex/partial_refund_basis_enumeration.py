from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PartialRefundBasisEnumeration(Enum):
    """
    Allowed values for Refund Basis.

    :cvar UNUSED_DAYS: Refund is given for any unused days.
    :cvar UNUSED_WEEKS: Refund is given for any unused weeks
    :cvar UNUSED_MONTHS: Refund is given for any unused months
    :cvar UNUSED_SEMESTERS:
    :cvar OTHER: Other basis.
    """
    UNUSED_DAYS = "unusedDays"
    UNUSED_WEEKS = "unusedWeeks"
    UNUSED_MONTHS = "unusedMonths"
    UNUSED_SEMESTERS = "unusedSemesters"
    OTHER = "other"
