from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseEnumeration(Enum):
    """
    Allowed values for Stop Use.

    :cvar ACCESS: Stop May be used to access transport system.
    :cvar INTERCHANGE_ONLY: Stop may only be used for interchange.
        Passengers may not enter or exit the station.
    :cvar PASSTHROUGH: Vehicle passes through without stopping.
    :cvar NO_BOARDING_OR_ALIGHTING:
    """
    ACCESS = "access"
    INTERCHANGE_ONLY = "interchangeOnly"
    PASSTHROUGH = "passthrough"
    NO_BOARDING_OR_ALIGHTING = "noBoardingOrAlighting"
