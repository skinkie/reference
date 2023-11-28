from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ViaTypeEnumeration(Enum):
    """
    Allowed values Classification of Via.
    """
    STOP_POINT = "stopPoint"
    NAME = "name"
    OTHER = "other"
