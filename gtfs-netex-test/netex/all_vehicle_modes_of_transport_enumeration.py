from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AllVehicleModesOfTransportEnumeration(Enum):
    """Allowed values for MODES of Transport : TPEG pti_table 01.

    :cvar ALL:
    :cvar UNKNOWN:
    :cvar BUS:
    :cvar TROLLEY_BUS:
    :cvar TRAM:
    :cvar COACH:
    :cvar RAIL:
    :cvar INTERCITY_RAIL:
    :cvar URBAN_RAIL:
    :cvar METRO:
    :cvar AIR:
    :cvar WATER:
    :cvar CABLEWAY:
    :cvar FUNICULAR:
    :cvar SNOW_AND_ICE:
    :cvar TAXI:
    :cvar FERRY:
    :cvar LIFT:
    :cvar SELF_DRIVE: See pti12_x.
    :cvar ANY_MODE:
    :cvar OTHER:
    """
    ALL = "all"
    UNKNOWN = "unknown"
    BUS = "bus"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITY_RAIL = "intercityRail"
    URBAN_RAIL = "urbanRail"
    METRO = "metro"
    AIR = "air"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    SNOW_AND_ICE = "snowAndIce"
    TAXI = "taxi"
    FERRY = "ferry"
    LIFT = "lift"
    SELF_DRIVE = "selfDrive"
    ANY_MODE = "anyMode"
    OTHER = "other"
