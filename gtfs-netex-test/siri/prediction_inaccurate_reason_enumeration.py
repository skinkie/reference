from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictionInaccurateReasonEnumeration(Enum):
    VEHICLE_IN_TRAFFIC_JAM = "vehicleInTrafficJam"
    TECHNICAL_PROBLEM = "technicalProblem"
    DISPATCH_ACTION = "dispatchAction"
    MISSING_UPDATE = "missingUpdate"
    UNKNOWN = "unknown"
