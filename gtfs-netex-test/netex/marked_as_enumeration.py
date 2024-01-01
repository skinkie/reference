from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkedAsEnumeration(Enum):
    UNUSED = "unused"
    ACTIVATED = "activated"
    MARKED = "marked"
    USED = "used"
    EXPIRED = "expired"
