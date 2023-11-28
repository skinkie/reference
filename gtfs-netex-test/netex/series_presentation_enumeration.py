from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesPresentationEnumeration(Enum):
    """
    Allowed values for Fare Point Presentation.
    """
    NONE = "none"
    REQUIRED = "required"
    OPTIONAL_LEFT = "optionalLeft"
    OPTIONAL_RIGHT = "optionalRight"
