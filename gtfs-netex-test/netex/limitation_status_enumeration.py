from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LimitationStatusEnumeration(Enum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    PARTIAL = "partial"
