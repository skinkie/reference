from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LicenceRequirementsEnumeration(Enum):
    FULL = "full"
    PROVISIONAL = "provisional"
    ADDITIONAL = "additional"
    NONE = "none"
