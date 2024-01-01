from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TariffBasisEnumeration(Enum):
    FLAT = "flat"
    DISTANCE = "distance"
    UNIT_SECTION = "unitSection"
    ZONE = "zone"
    ZONE_TO_ZONE = "zoneToZone"
    POINT_TO_POINT = "pointToPoint"
    ROUTE = "route"
    TOUR = "tour"
    GROUP = "group"
    DISCOUNT = "discount"
    PERIOD = "period"
    FREE = "free"
    OTHER = "other"
