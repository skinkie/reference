from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PathDirectionEnumeration(Enum):
    ONE_WAY = "oneWay"
    TWO_WAY = "twoWay"
