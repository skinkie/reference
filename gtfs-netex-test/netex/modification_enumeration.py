from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationEnumeration(Enum):
    NEW = "new"
    REVISE = "revise"
    DELETE = "delete"
    UNCHANGED = "unchanged"
    DELTA = "delta"
