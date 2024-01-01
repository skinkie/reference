from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class JourneyAccountingEnumeration(Enum):
    CONTRACT = "contract"
    SUBSIDY = "subsidy"
    OTHER = "other"
