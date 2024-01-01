from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseActionEnumeration(Enum):
    PURCHASE = "purchase"
    ORDER_WITHOUT_PAYMENT = "orderWithoutPayment"
    RESERVE = "reserve"
    PAY_FOR_PREVIOUS_ORDER = "payForPreviousOrder"
    SUBSCRIBE = "subscribe"
    PAY_INSTALLMENT = "payInstallment"
    OTHER = "other"
