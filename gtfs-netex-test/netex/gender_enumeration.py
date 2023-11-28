from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GenderEnumeration(Enum):
    """
    Allowed values for Gender.
    """
    FEMALE = "female"
    MALE = "male"
    UNSPECIFIED = "unspecified"
