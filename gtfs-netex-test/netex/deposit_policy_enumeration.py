from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DepositPolicyEnumeration(Enum):
    NONE = "none"
    DEPOSIT_TAKEN = "depositTaken"
    DEPOSIT_BLOCKED = "depositBlocked"
    OTHER = "other"
