from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PlaceUseEnumeration(Enum):
    START_AT = "startAt"
    END_AT = "endAt"
    VIA = "via"
    RESTRICT_TO = "restrictTo"
    OTHER = "other"
