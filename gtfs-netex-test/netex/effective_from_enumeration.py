from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EffectiveFromEnumeration(Enum):
    """
    Allowed values for EffectiveFrom.
    """
    NEVER = "never"
    NEXT_INTERVAL = "nextInterval"
    NEXT_INSTALLMENT = "nextInstallment"
    ANY_TIME = "anyTime"
    OTHER = "other"
