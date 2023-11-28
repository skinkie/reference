from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnCeasingEnumeration(Enum):
    """
    Allowed values for Ceasing  to be Eligible + v1.1.

    :cvar IMMEDIATE_TERMINATION: If user ceases to be eligible,
        automatically terminate validity of an  elibility dependent
        product.
    :cvar USE_UNTIL_EXPIRY: If user ceases to be eligible, they may go
        on using the product until it  expires..
    :cvar TERMINATE_AFTER_GRACE_PERIOD: If user ceases to be eligible,
        termination  take place after the end of a grace period
    :cvar AUTOMATICALLY_SUBSTITUTE_PRODUCT:
    :cvar NO_ACTION: If user ceases to be eligible, automatically
        substitute them with an appropiate  replacement product.
    :cvar OTHER:
    """
    IMMEDIATE_TERMINATION = "immediateTermination"
    USE_UNTIL_EXPIRY = "useUntilExpiry"
    TERMINATE_AFTER_GRACE_PERIOD = "terminateAfterGracePeriod"
    AUTOMATICALLY_SUBSTITUTE_PRODUCT = "automaticallySubstituteProduct"
    NO_ACTION = "noAction"
    OTHER = "other"
