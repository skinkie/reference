from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TimingPointStatusEnumeration(Enum):
    TIMING_POINT = "timingPoint"
    SECONDARY_TIMING_POINT = "secondaryTimingPoint"
    NOT_TIMING_POINT = "notTimingPoint"
