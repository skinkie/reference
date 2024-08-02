from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ServiceExceptionEnumeration(Enum):
    BEFORE_FIRST_JOURNEY = "beforeFirstJourney"
    AFTER_LAST_JOURNEY = "afterLastJourney"
    NO_SERVICE_TODAY = "noServiceToday"
    TRANSPORT_TEMPORARILY_SUSPENDED = "transportTemporarilySuspended"
    TRANSPORT_LONGTERM_SUSPENDED = "transportLongtermSuspended"
    TRANSPORT_SEVERLY_DISRUPTED = "transportSeverlyDisrupted"
    REALTIME_DATA_NOT_AVAILABLE = "realtimeDataNotAvailable"
    REALTIME_DATA_AVAILABLE = "realtimeDataAvailable"
