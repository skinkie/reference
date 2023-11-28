from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceNeededEnumeration(Enum):
    """
    Allowed values for  assistance needed.
    """
    LEVEL_ACCESS = "levelAccess"
    STEP_NEGOTIATION = "stepNegotiation"
    RAMP_REQUIRED = "rampRequired"
    HOIST_REQUIRED = "hoistRequired"
    UNKNOWN = "unknown"
