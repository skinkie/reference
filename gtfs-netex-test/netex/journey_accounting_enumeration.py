from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class JourneyAccountingEnumeration(Enum):
    """
    Allowed values for Accounting Coverage.

    :cvar CONTRACT: ERA X01: The connection is guaranteed under any
        circumstances.
    :cvar SUBSIDY: ERA X02: The connection is normally guaranteed,
        although the connection time available is shorter than the
        location connection time.
    :cvar OTHER: ERA X03: The connection is not guaranteed, although the
        connection time available is longer than the location connection
        time.
    """
    CONTRACT = "contract"
    SUBSIDY = "subsidy"
    OTHER = "other"
