from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AudioAnnouncementTypeEnumeration(Enum):
    """
    Allowed values for AudioAnnouncements.
    """
    ON_DEMAND = "onDemand"
    AUTOMATIC = "automatic"
