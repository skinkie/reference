from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LightingEnumeration(Enum):
    WELL_LIT = "wellLit"
    POORLY_LIT = "poorlyLit"
    UNLIT = "unlit"
    UNKNOWN = "unknown"
    OTHER = "other"
