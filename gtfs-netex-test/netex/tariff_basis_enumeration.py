from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TariffBasisEnumeration(Enum):
    """
    Allowed values for TariffBasis.

    :cvar FLAT: Tariff is flat, i.e. not based on spatial elements.
    :cvar DISTANCE: Tariff is based on spatial distance.
    :cvar UNIT_SECTION:
    :cvar ZONE: Tariff is based on use of specified zones.
    :cvar ZONE_TO_ZONE: Tariff is based on specified zone to zone
        transitions.
    :cvar POINT_TO_POINT: Tariff is based on specified point to point
        transitions.
    :cvar ROUTE: Tariff is based on specific routes, eg. for SERIES
        CONSTRAINTs.
    :cvar TOUR: Tariff is based on a specific tour.
    :cvar GROUP: Tariff is based on size of group.
    :cvar DISCOUNT: Tariff is for discount rates.
    :cvar PERIOD: Tariff is based on temporal durtaions, e.g minutes or
        days of travel.
    :cvar FREE: Tariff is free to user.
    :cvar OTHER: Other Tariff Basis.
    """
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
