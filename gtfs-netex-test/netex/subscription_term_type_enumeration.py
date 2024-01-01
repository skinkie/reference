from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionTermTypeEnumeration(Enum):
    FIXED = "fixed"
    VARIABLE = "variable"
    OPEN_ENDED = "openEnded"
