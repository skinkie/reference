from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundTripTypeEnumeration(Enum):
    SINGLE = "single"
    RETURN = "return"
    RETURN_OUT = "returnOut"
    RETURN_BACK = "returnBack"
    RETURN_ONLY = "returnOnly"
    MULTIPLE = "multiple"
