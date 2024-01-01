from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketValidatorEnumeration(Enum):
    PAPER_STAMP = "paperStamp"
    CONTACT_LESS = "contactLess"
    MAGNETIC = "magnetic"
    OTHER = "other"
