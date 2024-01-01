from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceAvailabilityEnumeration(Enum):
    NONE = "none"
    AVAILABLE = "available"
    AVAILABLE_IF_BOOKED = "availableIfBooked"
    AVAILABLE_AT_CERTAIN_TIMES = "availableAtCertainTimes"
    UNKNOWN = "unknown"
