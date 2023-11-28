from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingTypeEnumeration(Enum):
    """
    Allowed value for type of locking mechanism.+v1.1.
    """
    KEY = "key"
    KEYBOARD = "keyboard"
    MECHANICAL_NUMBERING = "mechanicalNumbering"
    CONTACTLESS = "contactless"
    MOBILE_APP = "mobileApp"
    OTHER = "other"
