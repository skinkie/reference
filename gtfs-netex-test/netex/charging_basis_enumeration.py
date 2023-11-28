from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChargingBasisEnumeration(Enum):
    """
    Allowed values for TariffBasis.
    """
    NORMAL_FARE = "normalFare"
    DISCOUNTED = "discounted"
    FREE = "free"
    VARIOUS = "various"
    ANY = "any"
