from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseActionEnumeration(Enum):
    """
    Allowed values for Purchase Action +v1.1.

    :cvar PURCHASE: Purchase and payment.
    :cvar ORDER_WITHOUT_PAYMENT: Purchase with deferred  payment.
    :cvar RESERVE: Reervation but not necessarily payment
    :cvar PAY_FOR_PREVIOUS_ORDER: Payment for previously ordered
        service.
    :cvar SUBSCRIBE:
    :cvar PAY_INSTALLMENT:
    :cvar OTHER:
    """
    PURCHASE = "purchase"
    ORDER_WITHOUT_PAYMENT = "orderWithoutPayment"
    RESERVE = "reserve"
    PAY_FOR_PREVIOUS_ORDER = "payForPreviousOrder"
    SUBSCRIBE = "subscribe"
    PAY_INSTALLMENT = "payInstallment"
    OTHER = "other"
