from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionRenewalPolicyEnumeration(Enum):
    """
    Allowed values for SUBSCRIBING Renewal Policy.

    :cvar AUTOMATIC: Renew automatcally at end of term.
    :cvar MANUAL: Renew on request.
    :cvar AUTOMATIC_ON_CONFIRMATION: Confirm and renew automatcally at
        end of  subscription term.
    :cvar NONE: No renewal allowed.
    :cvar OTHER:
    """
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    AUTOMATIC_ON_CONFIRMATION = "automaticOnConfirmation"
    NONE = "none"
    OTHER = "other"
