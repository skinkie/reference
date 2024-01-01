from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TimeOfDayEnumeration(Enum):
    DAWN = "dawn"
    DUSK = "dusk"
    NOON = "noon"
    MIDNIGHT = "midnight"
    CURFEW_START = "curfewStart"
    CURFEW_END = "curfewEnd"
