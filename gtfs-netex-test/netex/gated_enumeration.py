from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GatedEnumeration(Enum):
    GATED_AREA = "gatedArea"
    OPEN_AREA = "openArea"
    UNKNOWN = "unknown"
