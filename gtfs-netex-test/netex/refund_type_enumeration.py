from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RefundTypeEnumeration(Enum):
    """
    Allowed values for Refunding Type.

    :cvar UNUSED: Refund for unused ticket or pass.
    :cvar DELAY: Refund is for delayed journey.
    :cvar CANCELLATION: Refund is for cancelled journey.
    :cvar PARTIAL_JOURNEY: Refund is for unusued section of a journey.
    :cvar EARLY_TERMINATION: Partial refund is for  early termination of
        a period pass or season ticket.
    :cvar CHANGE_OF_GROUP_SIZE: Refund for change of group size.
    :cvar OTHER:
    """
    UNUSED = "unused"
    DELAY = "delay"
    CANCELLATION = "cancellation"
    PARTIAL_JOURNEY = "partialJourney"
    EARLY_TERMINATION = "earlyTermination"
    CHANGE_OF_GROUP_SIZE = "changeOfGroupSize"
    OTHER = "other"
