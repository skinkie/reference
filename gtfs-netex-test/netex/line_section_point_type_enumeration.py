from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineSectionPointTypeEnumeration(Enum):
    """
    Allowed values for a type of section point.
    """
    NORMAL = "normal"
    INTERCHANGE = "interchange"
    MAJOR_INTERCHANGE = "majorInterchange"
    TERMINUS = "terminus"
    MAJOR_TERMINUS = "majorTerminus"
    OTHER = "other"
