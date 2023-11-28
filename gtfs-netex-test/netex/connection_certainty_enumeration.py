from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ConnectionCertaintyEnumeration(Enum):
    """
    Allowed values for  Guaranteed.

    :cvar GUARANTEED: ERA X01: The connection is guaranteed under any
        circumstances.
    :cvar NORMALLY_GUARANTEED: ERA X02: The connection is normally
        guaranteed, although the connection time available is shorter
        than the location connection time.
    :cvar NOT_GUARANTEED: ERA X03: The connection is not guaranteed,
        although the connection time available is longer than the
        location connection time.
    :cvar NEVER_GUARANTEED: ERA X04: The connection is never guaranteed,
        although the connection time available is longer than the
        location connection time.
    """
    GUARANTEED = "guaranteed"
    NORMALLY_GUARANTEED = "normallyGuaranteed"
    NOT_GUARANTEED = "notGuaranteed"
    NEVER_GUARANTEED = "neverGuaranteed"
