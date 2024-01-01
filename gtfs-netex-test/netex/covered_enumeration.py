from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CoveredEnumeration(Enum):
    INDOORS = "indoors"
    OUTDOORS = "outdoors"
    COVERED = "covered"
    MIXED = "mixed"
    UNKNOWN = "unknown"
