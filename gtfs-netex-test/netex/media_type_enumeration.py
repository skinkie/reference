from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MediaTypeEnumeration(Enum):
    NONE = "none"
    PAPER_TICKET = "paperTicket"
    PAPER_TICKET_WITH_COUPONS = "paperTicketWithCoupons"
    COUPON = "coupon"
    SELF_PRINT_PAPER_TICKET = "selfPrintPaperTicket"
    SMART_CARD = "smartCard"
    MOBILE_APP = "mobileApp"
    LICENCE_PLATE = "licencePlate"
    CARD = "card"
    MMS = "mms"
    SMS = "sms"
    OTHER = "other"
