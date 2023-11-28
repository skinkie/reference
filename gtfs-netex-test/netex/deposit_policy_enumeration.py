from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DepositPolicyEnumeration(Enum):
    """Allowed values for  Deposit  Policy.

    +v1.1.2

    :cvar NONE: No deposit required.
    :cvar DEPOSIT_TAKEN: Deposit charged and later refunded.
    :cvar DEPOSIT_BLOCKED: Deposit amount blocked on card but not
        subtracted.
    :cvar OTHER: Other policy.
    """
    NONE = "none"
    DEPOSIT_TAKEN = "depositTaken"
    DEPOSIT_BLOCKED = "depositBlocked"
    OTHER = "other"
