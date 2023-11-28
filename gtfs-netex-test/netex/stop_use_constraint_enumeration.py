from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseConstraintEnumeration(Enum):
    """
    Allowed values for Stop use constraint.
    """
    ARRIVING = "arriving"
    DEPARTING = "departing"
    PASSING_THROUGH = "passingThrough"
