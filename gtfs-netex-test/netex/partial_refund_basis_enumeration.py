from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PartialRefundBasisEnumeration(Enum):
    UNUSED_DAYS = "unusedDays"
    UNUSED_WEEKS = "unusedWeeks"
    UNUSED_MONTHS = "unusedMonths"
    UNUSED_SEMESTERS = "unusedSemesters"
    OTHER = "other"
