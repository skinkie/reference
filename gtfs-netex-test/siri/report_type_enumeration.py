from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ReportTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    INCIDENT = "incident"
    GENERAL = "general"
    OPERATOR = "operator"
    NETWORK = "network"
    STATION_TERMINAL = "stationTerminal"
    STOP_POINT = "stopPoint"
    CONNECTION_LINK = "connectionLink"
    POINT = "point"
    ROUTE = "route"
    INDIVIDUAL_SERVICE = "individualService"
    UNDEFINED = "undefined"
