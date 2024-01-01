from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DriverTypeFeeBasisEnumeration(Enum):
    FREE = "free"
    PER_ADDTIONAL_DRIVER = "perAddtionalDriver"
    OTHER = "other"
