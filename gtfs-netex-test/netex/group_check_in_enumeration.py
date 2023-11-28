from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupCheckInEnumeration(Enum):
    """
    Allowed values for GROUP CHECK IN.
    """
    NONE = "none"
    REQUIRED = "required"
    ALLOWED = "allowed"
