from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccountStatusTypeEnumeration(Enum):
    UNUSED = "unused"
    UNVERIFIED = "unverified"
    ACTIVE = "active"
    DORMANT = "dormant"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"
    CLOSED = "closed"
