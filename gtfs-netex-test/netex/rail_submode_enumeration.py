from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RailSubmodeEnumeration(Enum):
    """Values for Rail MODEs of TRANSPORT: TPEG pti_table_02, train link loc_table_13.

    :cvar UNKNOWN:
    :cvar LOCAL:
    :cvar HIGH_SPEED_RAIL: See ERA B.4.7009 - Name: Item description
        code: (8 high speed train). Long distance train formed by a unit
        capable for high speed running on high speed or normal lines
        most modern train unit
    :cvar SUBURBAN_RAILWAY: See ERA B.4.7009 - Name: Item description
        code: . (12 suburban) Regional train organised by the regional
        government public transport in and around cities, running on its
        own freeways underground or overground, operational running with
        signals
    :cvar REGIONAL_RAIL: See ERA B.4.7009 - Name: Item description code.
        (11 Regional) Regional train organised by the regional
        government even if formed by a unit capable for high speed
        running on high speed lines
    :cvar INTERREGIONAL_RAIL: See ERA B.4.7009 - Name: Item description
        code: (10 Interregional) Regional train running in more than one
        region.
    :cvar LONG_DISTANCE: See ERA B.4.7009 - Name: Item description code:
        (9 Intercity). Long distance train formed by a unit capable for
        high speed or not running on high speed or normal lines modern
        train unit high quality service restricted stopping pattern
    :cvar INTERNATIONAL:
    :cvar SLEEPER_RAIL_SERVICE:
    :cvar NIGHT_RAIL:
    :cvar CAR_TRANSPORT_RAIL_SERVICE: See ERA B.4.7009 - Name: Item
        description code: (14 Motor rail) Service transporting
        passenger's motor vehicle passengers are admitted either with
        vehicle only or with or without vehicle Service mode
    :cvar TOURIST_RAILWAY: See ERA B.4.7009 - Name: Item description
        code: (16 Historic train).
    :cvar AIRPORT_LINK_RAIL:
    :cvar RAIL_SHUTTLE:
    :cvar REPLACEMENT_RAIL_SERVICE:
    :cvar SPECIAL_TRAIN:
    :cvar CROSS_COUNTRY_RAIL:
    :cvar RACK_AND_PINION_RAILWAY: See ERA B.4.7009 - Name: Item
        description code: (15 Mountain train) Local train adapted for
        running in mountain railway lines.
    """
    UNKNOWN = "unknown"
    LOCAL = "local"
    HIGH_SPEED_RAIL = "highSpeedRail"
    SUBURBAN_RAILWAY = "suburbanRailway"
    REGIONAL_RAIL = "regionalRail"
    INTERREGIONAL_RAIL = "interregionalRail"
    LONG_DISTANCE = "longDistance"
    INTERNATIONAL = "international"
    SLEEPER_RAIL_SERVICE = "sleeperRailService"
    NIGHT_RAIL = "nightRail"
    CAR_TRANSPORT_RAIL_SERVICE = "carTransportRailService"
    TOURIST_RAILWAY = "touristRailway"
    AIRPORT_LINK_RAIL = "airportLinkRail"
    RAIL_SHUTTLE = "railShuttle"
    REPLACEMENT_RAIL_SERVICE = "replacementRailService"
    SPECIAL_TRAIN = "specialTrain"
    CROSS_COUNTRY_RAIL = "crossCountryRail"
    RACK_AND_PINION_RAILWAY = "rackAndPinionRailway"
