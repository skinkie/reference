from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FontSizeEnumeration(Enum):
    """Allowed values for size of font.

    +v1.1
    """
    VERY_SMALL = "verySmall"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    VERY_LARGE = "veryLarge"
