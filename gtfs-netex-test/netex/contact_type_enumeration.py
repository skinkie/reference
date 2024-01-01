from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContactTypeEnumeration(Enum):
    ANY = "any"
    INFORMATION = "information"
    RESERVATIONS = "reservations"
    LOST_PROPERTY = "lostProperty"
    PUBLIC_RELATIONS = "publicRelations"
    COMPLAINTS = "complaints"
    EMERGENCY = "emergency"
    OTHER = "other"
