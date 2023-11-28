from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AdditionalDriverTypeEnumeration(Enum):
    """
    Allowed values for ADDITIONAL DRIVER   Type.
    """
    NONE = "none"
    NAMED = "named"
    ANY = "any"
    OTHER = "other"
