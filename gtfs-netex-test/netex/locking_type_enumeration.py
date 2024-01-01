from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingTypeEnumeration(Enum):
    KEY = "key"
    KEYBOARD = "keyboard"
    MECHANICAL_NUMBERING = "mechanicalNumbering"
    CONTACTLESS = "contactless"
    MOBILE_APP = "mobileApp"
    OTHER = "other"
