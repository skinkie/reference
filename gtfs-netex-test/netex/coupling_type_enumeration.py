from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CouplingTypeEnumeration(Enum):
    """
    Values for Coupling Types +v1.2.2.
    """
    UNDEFINED = "undefined"
    PLUG = "plug"
    PANTOGRAPH_ABOVE = "pantographABove"
    INDUCTION = "induction"
    OTHER = "other"
