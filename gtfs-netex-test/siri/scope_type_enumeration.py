from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ScopeTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    STOP_PLACE = "stopPlace"
    LINE = "line"
    ROUTE = "route"
    PUBLIC_TRANSPORT_SERVICE = "publicTransportService"
    OPERATOR = "operator"
    CITY = "city"
    AREA = "area"
    STOP_POINT = "stopPoint"
    STOP_PLACE_COMPONENT = "stopPlaceComponent"
    PLACE = "place"
    NETWORK = "network"
    VEHICLE_JOURNEY = "vehicleJourney"
    DATED_VEHICLE_JOURNEY = "datedVehicleJourney"
    CONNECTION_LINK = "connectionLink"
    INTERCHANGE = "interchange"
    ALL_PT = "allPT"
    GENERAL = "general"
    ROAD = "road"
    UNDEFINED = "undefined"
