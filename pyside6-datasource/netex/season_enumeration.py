from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeasonEnumeration(Enum):
    """
    Allowed values for Season.
    """
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"
    PERENNIALLY = "Perennially"
