from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareBasisEnumeration(Enum):
    """
    Allowed values for Fare Basis.
    """
    ROUTE = "route"
    DISTANCE = "distance"
