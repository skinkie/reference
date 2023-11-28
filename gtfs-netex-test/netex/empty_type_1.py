from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EmptyType1(Enum):
    """
    A type with no allowed content, used when simply the presence of an element is
    significant.
    """
    VALUE = ""
