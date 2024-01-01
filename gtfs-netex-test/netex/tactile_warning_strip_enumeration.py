from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TactileWarningStripEnumeration(Enum):
    TACTILE_STRIP_AT_BEGINNING = "tactileStripAtBeginning"
    TACTILE_STRIP_AT_END = "tactileStripAtEnd"
    TACTILE_STRIP_AT_BOTH_ENDS = "tactileStripAtBothEnds"
    NO_TACTILE_STRIP = "noTactileStrip"
    UNKNOWN = "unknown"
