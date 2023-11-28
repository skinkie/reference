from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TimingPointStatusEnumeration(Enum):
    """
    Allowed values for TYPE OF TIMING POINT.
    """
    TIMING_POINT = "timingPoint"
    SECONDARY_TIMING_POINT = "secondaryTimingPoint"
    NOT_TIMING_POINT = "notTimingPoint"
