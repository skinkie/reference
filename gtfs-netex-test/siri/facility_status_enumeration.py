from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FacilityStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    PARTIALLY_AVAILABLE = "partiallyAvailable"
    ADDED = "added"
    REMOVED = "removed"
