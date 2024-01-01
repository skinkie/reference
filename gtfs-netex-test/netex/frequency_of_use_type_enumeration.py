from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrequencyOfUseTypeEnumeration(Enum):
    NONE = "none"
    UNLIMITED = "unlimited"
    LIMITED = "limited"
    TWICE_ADAY = "twiceADay"
    SINGLE = "single"
