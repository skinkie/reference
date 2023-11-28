from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccountStatusTypeEnumeration(Enum):
    """
    Allowed values for Account Status.
    """
    UNUSED = "unused"
    UNVERIFIED = "unverified"
    ACTIVE = "active"
    DORMANT = "dormant"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"
    CLOSED = "closed"
