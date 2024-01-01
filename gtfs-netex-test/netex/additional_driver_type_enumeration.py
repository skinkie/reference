from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AdditionalDriverTypeEnumeration(Enum):
    NONE = "none"
    NAMED = "named"
    ANY = "any"
    OTHER = "other"
