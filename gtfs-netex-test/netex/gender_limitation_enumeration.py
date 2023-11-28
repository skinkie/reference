from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GenderLimitationEnumeration(Enum):
    """
    Allowed values for GENDER LIMITATION.
    """
    BOTH = "both"
    FEMALE_ONLY = "femaleOnly"
    MALE_ONLY = "maleOnly"
    SAME_SEX_ONLY = "sameSexOnly"
