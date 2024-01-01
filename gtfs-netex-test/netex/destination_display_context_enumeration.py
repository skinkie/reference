from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DestinationDisplayContextEnumeration(Enum):
    ANY = "any"
    CONTINUE_TO = "continueTo"
    ENDS_AT = "endsAt"
    TRANSFER_AT = "transferAt"
    VIA = "via"
    IN_MESSAGE = "inMessage"
    UNKNOWN = "unknown"
