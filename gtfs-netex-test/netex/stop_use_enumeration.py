from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseEnumeration(Enum):
    ACCESS = "access"
    INTERCHANGE_ONLY = "interchangeOnly"
    PASSTHROUGH = "passthrough"
    NO_BOARDING_OR_ALIGHTING = "noBoardingOrAlighting"
