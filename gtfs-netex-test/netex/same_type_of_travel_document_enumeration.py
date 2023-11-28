from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfTravelDocumentEnumeration(Enum):
    """
    Allowed values for Type of Trave lDocument ENTITLEMENT CONSTRAINT.
    """
    ANY = "any"
    SAME = "same"
    SAME_MEDIA = "sameMedia"
    SAME_SMARTCARD = "sameSmartcard"
    SAME_MOBILE_APP = "sameMobileApp"
    DIFFERENT = "different"
