from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PenaltyPolicyTypeEnumeration(Enum):
    NO_TICKET = "noTicket"
    NO_CHECK_IN = "noCheckIn"
    NO_CHECK_OUT = "noCheckOut"
    NO_VALIDATION = "noValidation"
    OTHER = "other"
