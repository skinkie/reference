from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QueueManagementEnumeration(Enum):
    NONE = "none"
    MAZE = "maze"
    SEPARATE_LINES = "separateLines"
    TICKETED = "ticketed"
    OTHER = "other"
