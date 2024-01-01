from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class IntervalTypeEnumeration(Enum):
    STOP = "stop"
    TARIFF_ZONE = "tariffZone"
    DISTANCE = "distance"
    SECTION = "section"
    COUPON = "coupon"
    OTHER = "other"
