from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoutingTypeEnumeration(Enum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    BOTH = "both"
