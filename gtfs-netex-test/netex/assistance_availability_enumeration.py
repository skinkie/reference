from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceAvailabilityEnumeration(Enum):
    """
    Allowed values for  Assistance Availability.

    :cvar NONE: Assistance is not  available.
    :cvar AVAILABLE: Assistance is nornally available.
    :cvar AVAILABLE_IF_BOOKED: Assistance is  available if booked.
    :cvar AVAILABLE_AT_CERTAIN_TIMES: Assistance is   available at
        certain times.
    :cvar UNKNOWN: Not known if assistance is available.
    """
    NONE = "none"
    AVAILABLE = "available"
    AVAILABLE_IF_BOOKED = "availableIfBooked"
    AVAILABLE_AT_CERTAIN_TIMES = "availableAtCertainTimes"
    UNKNOWN = "unknown"
