from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AdviceTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    USE_REPLACEMENT_BUS = "useReplacementBus"
    USE_REPLACEMENT_TRAIN = "useReplacementTrain"
    USE_ALTERNATIVE_ROUTE = "useAlternativeRoute"
    GO_ON_FOOT = "goOnFoot"
    DANGER_LEAVE_STATION = "dangerLeaveStation"
    NO_MEANS_OF_TRAVEL = "noMeansOfTravel"
    USE_DIFFERENT_STOPS = "useDifferentStops"
    USE_ALTERNATIVE_STOP = "useAlternativeStop"
    DANGER_DO_NOT_LEAVE_VEHICLE = "dangerDoNotLeaveVehicle"
    TAKE_ADVICE_ANNOUNCEMENTS = "takeAdviceAnnouncements"
    TAKE_ADVICE_PERSONNEL = "takeAdvicePersonnel"
    OBEY_ADVICE_POLICE = "obeyAdvicePolice"
    USE_OTHER_PT = "useOtherPT"
    USE_INTERCHANGE = "useInterchange"
    NO_ADVICE = "noAdvice"
    UNDEFINED_ADVICE = "undefinedAdvice"
    TAKE_DETOUR = "takeDetour"
    USE_ALTERNATIVE_ACCESS = "useAlternativeAccess"
