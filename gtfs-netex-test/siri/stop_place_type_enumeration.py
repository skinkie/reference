from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class StopPlaceTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    RAILWAY_STATION = "railwayStation"
    UNDERGROUND_STATION = "undergroundStation"
    TRAM_STATION = "tramStation"
    BUS_STATION = "busStation"
    AIRPORT = "airport"
    PIER = "pier"
    HARBOUR_PORT = "harbourPort"
    FERRY_STOP = "ferryStop"
    LIGHT_RAILWAY_STATION = "lightRailwayStation"
    COGWHEEL_STATION = "cogwheelStation"
    FUNICULAR_STATION = "funicularStation"
    ROPEWAY_STATION = "ropewayStation"
    COACH_STATION = "coachStation"
    FERRY_PORT = "ferryPort"
    ON_STREET_BUS = "onStreetBus"
    ON_STREET_TRAM = "onStreetTram"
    SKI_LIFT = "skiLift"
    OTHER = "other"
    UNDEFINED_STOP_PLACE_TYPE = "undefinedStopPlaceType"
    RAIL_STATION = "railStation"
    METRO_STATION = "metroStation"
