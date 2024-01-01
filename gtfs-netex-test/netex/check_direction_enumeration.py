from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckDirectionEnumeration(Enum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    BOTH_WAYS = "bothWays"
