from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EmptyType2(Enum):
    """
    A type with no allowed content, used when simply the presence of an element is
    significant.
    """
    VALUE = ""
