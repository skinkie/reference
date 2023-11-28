from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SharedUsageEnumeration(Enum):
    """
    Allowed values for Shared Usage.

    :cvar SINGLE_USER: Only one user may use the product at a time. E.g.
        a mobile app carnet of tickets may only restricted to  be used
        by the mobile device  holder.
    :cvar CONCURRENT_USERS: Several users  may use the same product at a
        time. E.g. a carnet of tickets may be shared with several  users
        other than the purchaser.
    :cvar CONCURRENT_DESIGNATED_USERS: Several users (but only of a
        specifed type of companion) may use the same product at a time.
        E.g.  a mobile app carnet of tickets may be shared with children
        but not others.
    """
    SINGLE_USER = "singleUser"
    CONCURRENT_USERS = "concurrentUsers"
    CONCURRENT_DESIGNATED_USERS = "concurrentDesignatedUsers"
