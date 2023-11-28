from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingChargeTypeEnumeration(Enum):
    """
    Allowed values for BookingPayment +v1.1.

    :cvar FULL_AMOUNT: Purchase and payment.
    :cvar BLOCK_FULL_AMOUNT_ON_CARD:
    :cvar DEPOSIT: Purchase with deferred  payment.
    :cvar NONE:
    :cvar OTHER: Reervation but not necessarily payment
    """
    FULL_AMOUNT = "fullAmount"
    BLOCK_FULL_AMOUNT_ON_CARD = "blockFullAmountOnCard"
    DEPOSIT = "deposit"
    NONE = "none"
    OTHER = "other"
