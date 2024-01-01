from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MinimumStayTypeEnumeration(Enum):
    NONE = "none"
    SPECIFIED_NIGHTS_AWAY = "specifiedNightsAway"
    COUNT_NIGHTS_AWAY = "countNightsAway"
    BOTH = "both"
    EITHER = "either"
