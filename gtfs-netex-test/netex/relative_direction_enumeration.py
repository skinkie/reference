from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelativeDirectionEnumeration(Enum):
    """
    Allowed values for RELATIVE DIRECTIONS.
    """
    BOTH = "both"
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
