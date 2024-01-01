from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainSizeEnumeration(Enum):
    NORMAL = "normal"
    SHORT = "short"
    LONG = "long"
