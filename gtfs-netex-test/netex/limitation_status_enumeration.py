from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LimitationStatusEnumeration(Enum):
    """
    Allowed values for an accessibility value.

    :cvar TRUE: All of PLACE is accessible for criteria.
    :cvar FALSE: PLACE is not considered to meet accessibility criteria.
    :cvar UNKNOWN: It is not known whether PLACE meets accessibility
        criteria.
    :cvar PARTIAL: Some areas of PLACE are not considered to meet
        accessibility criteria.
    """
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    PARTIAL = "partial"
