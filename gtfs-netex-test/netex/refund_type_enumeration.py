from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RefundTypeEnumeration(Enum):
    UNUSED = "unused"
    DELAY = "delay"
    CANCELLATION = "cancellation"
    PARTIAL_JOURNEY = "partialJourney"
    EARLY_TERMINATION = "earlyTermination"
    CHANGE_OF_GROUP_SIZE = "changeOfGroupSize"
    OTHER = "other"
