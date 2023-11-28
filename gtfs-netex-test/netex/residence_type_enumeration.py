from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResidenceTypeEnumeration(Enum):
    """
    Allowed values for RESIDENCE TYPE.
    """
    LIVE = "live"
    WORK = "work"
    STUDY = "study"
    EXCHANGE = "exchange"
    BORN = "born"
    NON_RESIDENT = "nonResident"
