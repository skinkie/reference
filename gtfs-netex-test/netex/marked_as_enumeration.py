from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkedAsEnumeration(Enum):
    """
    Allowed values for MarkedAs Status.++ +v1.1.
    """
    UNUSED = "unused"
    ACTIVATED = "activated"
    MARKED = "marked"
    USED = "used"
    EXPIRED = "expired"
