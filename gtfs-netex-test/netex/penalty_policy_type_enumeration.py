from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PenaltyPolicyTypeEnumeration(Enum):
    """
    Allowed values for Penalty Policy Type.
    """
    NO_TICKET = "noTicket"
    NO_CHECK_IN = "noCheckIn"
    NO_CHECK_OUT = "noCheckOut"
    NO_VALIDATION = "noValidation"
    OTHER = "other"
