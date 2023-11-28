from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameJourneyEnumeration(Enum):
    """
    Allowed values for Journey ENTITLEMENT CONSTRAINT.
    """
    ANY = "any"
    SAME = "same"
    SIMILAR = "similar"
    DIFFERENT = "different"
