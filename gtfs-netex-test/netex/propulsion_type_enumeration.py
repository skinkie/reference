from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PropulsionTypeEnumeration(Enum):
    """
    Allowed values for type of power  +v1/2/2.
    """
    COMBUSTION = "combustion"
    ELECTRIC = "electric"
    ELECTRIC_ASSIST = "electricAssist"
    HYBRID = "hybrid"
    HUMAN = "human"
    OTHER = "other"
