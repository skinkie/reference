from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CoveredEnumeration(Enum):
    """
    Allowed values for covered.
    """
    INDOORS = "indoors"
    OUTDOORS = "outdoors"
    COVERED = "covered"
    MIXED = "mixed"
    UNKNOWN = "unknown"
