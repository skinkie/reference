from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ServiceConditionEnumeration(Enum):
    UNKNOWN = "unknown"
    DELAY = "delay"
    MINOR_DELAYS = "minorDelays"
    MAJOR_DELAYS = "majorDelays"
    OPERATION_TIME_EXTENSION = "operationTimeExtension"
    ON_TIME = "onTime"
    DISTURBANCE_RECTIFIED = "disturbanceRectified"
    CHANGE_OF_PLATFORM = "changeOfPlatform"
    LINE_CANCELLATION = "lineCancellation"
    TRIP_CANCELLATION = "tripCancellation"
    BOARDING = "boarding"
    GO_TO_GATE = "goToGate"
    STOP_CANCELLED = "stopCancelled"
    STOP_MOVED = "stopMoved"
    STOP_ON_DEMAND = "stopOnDemand"
    ADDITIONAL_STOP = "additionalStop"
    SUBSTITUTED_STOP = "substitutedStop"
    DIVERTED = "diverted"
    DISRUPTION = "disruption"
    LIMITED_OPERATION = "limitedOperation"
    DISCONTINUED_OPERATION = "discontinuedOperation"
    IRREGULAR_TRAFFIC = "irregularTraffic"
    WAGON_ORDER_CHANGED = "wagonOrderChanged"
    TRAIN_SHORTENED = "trainShortened"
    ADDITIONAL_RIDE = "additionalRide"
    REPLACEMENT_RIDE = "replacementRide"
    TEMPORARILY_NON_STOPPING = "temporarilyNonStopping"
    TEMPORARY_STOPPLACE = "temporaryStopplace"
    UNDEFINED_STATUS = "undefinedStatus"
    ALTERED = "altered"
    CANCELLED = "cancelled"
    DELAYED = "delayed"
    NO_SERVICE = "noService"
    DISRUPTED = "disrupted"
    ADDITIONAL_SERVICE = "additionalService"
    SPECIAL_SERVICE = "specialService"
    NORMAL_SERVICE = "normalService"
    INTERMITTENT_SERVICE = "intermittentService"
    SHORT_FORMED_SERVICE = "shortFormedService"
    FULL_LENGTH_SERVICE = "fullLengthService"
    EXTENDED_SERVICE = "extendedService"
    SPLITTING_TRAIN = "splittingTrain"
    REPLACEMENT_TRANSPORT = "replacementTransport"
    ARRIVES_EARLY = "arrivesEarly"
    SHUTTLE_SERVICE = "shuttleService"
    REPLACEMENT_SERVICE = "replacementService"
    UNDEFINED_SERVICE_INFORMATION = "undefinedServiceInformation"
