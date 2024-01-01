from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareDemandTypeEnumeration(Enum):
    PEAK = "peak"
    MIDDLE = "middle"
    OFF_PEAK = "offPeak"
    SUPER_OFF_PEAK = "superOffPeak"
    NIGHT = "night"
    SPECIAL_EVENT = "specialEvent"
