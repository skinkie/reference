from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionTypeEnumeration(Enum):
    """
    Allowed values for Types of VERSION.
    """
    POINT = "point"
    BASELINE = "baseline"
