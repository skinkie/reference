from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChargingBasisEnumeration(Enum):
    NORMAL_FARE = "normalFare"
    DISCOUNTED = "discounted"
    FREE = "free"
    VARIOUS = "various"
    ANY = "any"
