from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleInFormationStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    PARTIALLY_AVAILABLE = "partiallyAvailable"
    ADDED = "added"
    REMOVED = "removed"
    DEFECTIVE = "defective"
    CLOSED = "closed"
    BOOKED = "booked"
    NO_RESTAURANT_SERVICE = "noRestaurantService"
    OPEN = "open"
