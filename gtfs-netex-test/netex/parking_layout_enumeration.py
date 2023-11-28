from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingLayoutEnumeration(Enum):
    """
    Allowed values for PARKING Layout types.

    :cvar COVERED:
    :cvar OPEN_SPACE:
    :cvar MULTISTOREY:
    :cvar UNDERGROUND:
    :cvar ROADSIDE:
    :cvar UNDEFINED:
    :cvar OTHER:
    :cvar ON_PAVEMENT:
    :cvar CYCLE_HIRE: DEPRECATED 1.2.2 Use onPavement instead
    """
    COVERED = "covered"
    OPEN_SPACE = "openSpace"
    MULTISTOREY = "multistorey"
    UNDERGROUND = "underground"
    ROADSIDE = "roadside"
    UNDEFINED = "undefined"
    OTHER = "other"
    ON_PAVEMENT = "onPavement"
    CYCLE_HIRE = "cycleHire"
