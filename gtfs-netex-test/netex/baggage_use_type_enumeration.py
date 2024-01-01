from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BaggageUseTypeEnumeration(Enum):
    CARRY_ON = "carryOn"
    CHECK_IN = "checkIn"
    OVERSIZE_CHECK_IN = "oversizeCheckIn"
    BAGGAGE_COMPARTMENT = "baggageCompartment"
