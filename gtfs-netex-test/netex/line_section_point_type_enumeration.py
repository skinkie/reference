from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineSectionPointTypeEnumeration(Enum):
    NORMAL = "normal"
    INTERCHANGE = "interchange"
    MAJOR_INTERCHANGE = "majorInterchange"
    TERMINUS = "terminus"
    MAJOR_TERMINUS = "majorTerminus"
    OTHER = "other"
