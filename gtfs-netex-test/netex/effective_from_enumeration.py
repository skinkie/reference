from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EffectiveFromEnumeration(Enum):
    NEVER = "never"
    NEXT_INTERVAL = "nextInterval"
    NEXT_INSTALLMENT = "nextInstallment"
    ANY_TIME = "anyTime"
    OTHER = "other"
