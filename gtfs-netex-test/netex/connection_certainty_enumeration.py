from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ConnectionCertaintyEnumeration(Enum):
    GUARANTEED = "guaranteed"
    NORMALLY_GUARANTEED = "normallyGuaranteed"
    NOT_GUARANTEED = "notGuaranteed"
    NEVER_GUARANTEED = "neverGuaranteed"
