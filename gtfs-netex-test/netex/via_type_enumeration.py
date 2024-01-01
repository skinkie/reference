from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ViaTypeEnumeration(Enum):
    STOP_POINT = "stopPoint"
    NAME = "name"
    OTHER = "other"
