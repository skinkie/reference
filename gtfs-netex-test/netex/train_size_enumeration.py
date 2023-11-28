from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainSizeEnumeration(Enum):
    """
    Allowed values for TYPE OF TRAIIN ELEMENT.
    """
    NORMAL = "normal"
    SHORT = "short"
    LONG = "long"
