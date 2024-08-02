from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class EquipmentStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
