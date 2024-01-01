from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GenderLimitationEnumeration(Enum):
    BOTH = "both"
    FEMALE_ONLY = "femaleOnly"
    MALE_ONLY = "maleOnly"
    SAME_SEX_ONLY = "sameSexOnly"
