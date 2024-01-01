from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckServiceEnumeration(Enum):
    SELF_SERVICE = "selfService"
    COUNTER_SERVICE = "counterService"
    ANY_SERVICE = "anyService"
    OTHER = "other"
