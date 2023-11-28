from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrequencyOfUseTypeEnumeration(Enum):
    """
    Allowed values for FREQUENCY OF USE Type.

    :cvar NONE: Product may not be used within allowed period.
    :cvar UNLIMITED: Unlimted use may be made of the product within
        allowed period.
    :cvar LIMITED: Product may be used up to  a limited amount within
        allowed period.
    :cvar TWICE_ADAY: Product may be used twice a day within allowed
        period.
    :cvar SINGLE: Product may  be used once within allowed period.
    """
    NONE = "none"
    UNLIMITED = "unlimited"
    LIMITED = "limited"
    TWICE_ADAY = "twiceADay"
    SINGLE = "single"
