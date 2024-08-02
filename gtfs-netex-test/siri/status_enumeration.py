from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class StatusEnumeration(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
