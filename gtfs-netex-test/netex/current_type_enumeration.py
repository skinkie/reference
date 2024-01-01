from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CurrentTypeEnumeration(Enum):
    UNDEFINED = "undefined"
    VALUE_1_PHASE_AC = "1-PhaseAC"
    VALUE_3_PHASE_AC = "3-PhaseAC"
    DC = "DC"
