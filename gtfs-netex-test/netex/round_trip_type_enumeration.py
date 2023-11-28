from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundTripTypeEnumeration(Enum):
    """
    Allowed values for ROUND TRIP Type.

    :cvar SINGLE: Single trip
    :cvar RETURN: Return trip between the same origin and destination
    :cvar RETURN_OUT: Outward part of a return trip.
    :cvar RETURN_BACK: Return part of a return trip.
    :cvar RETURN_ONLY:
    :cvar MULTIPLE: Multtrip carnet.
    """
    SINGLE = "single"
    RETURN = "return"
    RETURN_OUT = "returnOut"
    RETURN_BACK = "returnBack"
    RETURN_ONLY = "returnOnly"
    MULTIPLE = "multiple"
