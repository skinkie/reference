from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageStartConstraintTypeEnumeration(Enum):
    VARIABLE = "variable"
    FIXED = "fixed"
    FIXED_WINDOW = "fixedWindow"
