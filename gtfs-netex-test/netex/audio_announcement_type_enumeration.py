from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AudioAnnouncementTypeEnumeration(Enum):
    ON_DEMAND = "onDemand"
    AUTOMATIC = "automatic"
