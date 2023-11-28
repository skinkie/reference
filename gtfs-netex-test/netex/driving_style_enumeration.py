from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DrivingStyleEnumeration(Enum):
    """Allowed values for DrivingStyle.

    +v1.2.2
    """
    SEDATE = "sedate"
    MODERATE = "moderate"
    FAST = "fast"
    OTHER = "other"
