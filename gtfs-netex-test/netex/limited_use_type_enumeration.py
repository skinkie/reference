from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LimitedUseTypeEnumeration(Enum):
    """
    Allowed values for Limited use.

    :cvar INTERCHANGE_ONLY: Stop may only be used for interchange, not
        for entrance or exit.
    :cvar NO_DIRECT_ROAD_ACCESS: Stop may not be reached from Road by a
        paved path.
    :cvar LONG_WALK_TO_ACCESS: Stop may only be accessed by a long
        (&gt;200m) walk from road.
    :cvar ISOLATED: Stop is an island or ferry stop that does not
        connect to rad network.
    :cvar LIMITED_SERVICE: Stop has a very limited service.
    :cvar OTHER:
    """
    INTERCHANGE_ONLY = "interchangeOnly"
    NO_DIRECT_ROAD_ACCESS = "noDirectRoadAccess"
    LONG_WALK_TO_ACCESS = "longWalkToAccess"
    ISOLATED = "isolated"
    LIMITED_SERVICE = "limitedService"
    OTHER = "other"
