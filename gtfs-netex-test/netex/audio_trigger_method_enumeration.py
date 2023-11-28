from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AudioTriggerMethodEnumeration(Enum):
    """
    Allowed values for AudioTriggersMethod.
    """
    PRESENCE_DETECTOR = "presenceDetector"
    MOBILE_APP = "mobileApp"
    INTERNET_PAGE = "internetPage"
    SPECIFIC_DEVICE = "specificDevice"
    PUSH_BUTTON = "pushButton"
    OTHER = "other"
