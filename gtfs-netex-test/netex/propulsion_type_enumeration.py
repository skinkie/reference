from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PropulsionTypeEnumeration(Enum):
    COMBUSTION = "combustion"
    ELECTRIC = "electric"
    ELECTRIC_ASSIST = "electricAssist"
    HYBRID = "hybrid"
    HUMAN = "human"
    OTHER = "other"
