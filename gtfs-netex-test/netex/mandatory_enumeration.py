from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MandatoryEnumeration(Enum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    NOT_ALLOWED = "notAllowed"
