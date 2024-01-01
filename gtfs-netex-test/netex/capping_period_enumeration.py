from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CappingPeriodEnumeration(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    NONE = "none"
