from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RechargingProcessEnumeration(Enum):
    CHANGE_BATTERIES = "changeBatteries"
    POWERCABLE = "powercable"
    PANTOGRAPH = "pantograph"
    OTHER = "other"
