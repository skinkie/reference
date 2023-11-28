from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PlaceUseEnumeration(Enum):
    """
    Allowed values for PlaceUsage.
    """
    START_AT = "startAt"
    END_AT = "endAt"
    VIA = "via"
    RESTRICT_TO = "restrictTo"
    OTHER = "other"
