from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MetroSubmodesOfTransportEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"
    ALL_RAIL_SERVICES = "allRailServices"
    METRO_SERVICE = "metroService"
    NIGHT_METRO_SERVICE = "nightMetroService"
    EXPRESS_METRO_SERVICE = "expressMetroService"
    UNDEFINED_URBAN_RAILWAY_SERVICE = "undefinedUrbanRailwayService"
    PTI4_0 = "pti4_0"
    PTI4_1 = "pti4_1"
    PTI4_2 = "pti4_2"
    PTI4_3 = "pti4_3"
    PTI4_4 = "pti4_4"
    PTI4_255 = "pti4_255"
