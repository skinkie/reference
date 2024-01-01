from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfTravelDocumentEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    SAME_MEDIA = "sameMedia"
    SAME_SMARTCARD = "sameSmartcard"
    SAME_MOBILE_APP = "sameMobileApp"
    DIFFERENT = "different"
