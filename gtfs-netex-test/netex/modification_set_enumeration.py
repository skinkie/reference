from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationSetEnumeration(Enum):
    ALL = "all"
    CHANGES_ONLY = "changesOnly"
