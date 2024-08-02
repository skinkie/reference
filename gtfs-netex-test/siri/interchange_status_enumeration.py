from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class InterchangeStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    CONNECTION = "connection"
    REPLACEMENT = "replacement"
    ALTERNATIVE = "alternative"
    CONNECTION_NOT_HELD = "connectionNotHeld"
    CONNECTION_HELD = "connectionHeld"
    STATUS_OF_CONNECTION_UNDECIDED = "statusOfConnectionUndecided"
    UNDEFINED_CROSS_REFERENCE_INFORMATION = "undefinedCrossReferenceInformation"
    CONNECTION_CHANGED = "connectionChanged"
    DISTRIBUTOR_WAIT_PROLONGED = "distributorWaitProlonged"
    DEPARTURE_PLATFORM_CHANGED = "departurePlatformChanged"
    EXTRA_INTERCHANGE = "extraInterchange"
    CANCELLED = "cancelled"
    FEEDER_ARRIVAL_CANCELLATION = "feederArrivalCancellation"
    DISTRIBUTOR_DEPARTURE_CANCELLATION = "distributorDepartureCancellation"
    STATUS_OF_CONENCTION_UNDECIDED = "statusOfConenctionUndecided"
