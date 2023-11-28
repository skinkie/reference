from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionTermTypeEnumeration(Enum):
    """
    Allowed values for  Billing Policy.

    :cvar FIXED: Subscription must be for a fixed term.
    :cvar VARIABLE: Subscription can be for  an arbitray term,
    :cvar OPEN_ENDED: Subscription term is open ended.
    """
    FIXED = "fixed"
    VARIABLE = "variable"
    OPEN_ENDED = "openEnded"
