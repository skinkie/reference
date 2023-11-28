from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OperatorActivitiesEnumeration(Enum):
    """
    Allowed values for Operator Activities.
    """
    PASSENGER = "passenger"
    FREIGHT = "freight"
    INFRASTRUCTURE = "infrastructure"
    OTHER = "other"
