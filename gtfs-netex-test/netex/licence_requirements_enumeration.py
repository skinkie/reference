from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LicenceRequirementsEnumeration(Enum):
    """
    Allowed values for licence requirements.
    """
    FULL = "full"
    PROVISIONAL = "provisional"
    ADDITIONAL = "additional"
    NONE = "none"
