from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnCeasingEnumeration(Enum):
    IMMEDIATE_TERMINATION = "immediateTermination"
    USE_UNTIL_EXPIRY = "useUntilExpiry"
    TERMINATE_AFTER_GRACE_PERIOD = "terminateAfterGracePeriod"
    AUTOMATICALLY_SUBSTITUTE_PRODUCT = "automaticallySubstituteProduct"
    NO_ACTION = "noAction"
    OTHER = "other"
