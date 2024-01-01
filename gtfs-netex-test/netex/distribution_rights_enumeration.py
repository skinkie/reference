from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DistributionRightsEnumeration(Enum):
    NONE = "none"
    SELL = "sell"
    EXCHANGE = "exchange"
    REFUND = "refund"
    INFORM = "inform"
    BOOK = "book"
    PRIVATE = "private"
    OTHER = "other"
