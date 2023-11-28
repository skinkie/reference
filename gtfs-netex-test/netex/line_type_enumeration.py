from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineTypeEnumeration(Enum):
    """Allowed values Classification of  LINE.

    +v1.1
    """
    LOCAL = "local"
    URBAN = "urban"
    LONG_DISTANCE = "longDistance"
    EXPRESS = "express"
    SEASONAL = "seasonal"
    REPLACEMENT = "replacement"
    FLEXIBLE = "flexible"
    OTHER = "other"
