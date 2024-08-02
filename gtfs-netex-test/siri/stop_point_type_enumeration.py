from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class StopPointTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    PLATFORM_NUMBER = "platformNumber"
    TERMINAL_GATE = "terminalGate"
    FERRY_BERTH = "ferryBerth"
    HARBOUR_PIER = "harbourPier"
    LANDING_STAGE = "landingStage"
    BUS_STOP = "busStop"
    UNDEFINED_STOP_POINT_TYPE = "undefinedStopPointType"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
