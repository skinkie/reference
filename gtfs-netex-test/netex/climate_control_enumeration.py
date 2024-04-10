from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ClimateControlEnumeration(Enum):
    UNKNOWN = "unknown"
    NONE = "none"
    AIR_CONDITIONING = "airConditioning"
    HEATING = "heating"
    NO_CONDITIONING = "noConditioning"
    WINDOWS_CAN_BE_OPENED = "windowsCanBeOpened"
    SEALED_WINDOWS = "sealedWindows"
    OTHER = "other"
