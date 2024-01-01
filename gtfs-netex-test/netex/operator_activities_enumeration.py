from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OperatorActivitiesEnumeration(Enum):
    PASSENGER = "passenger"
    FREIGHT = "freight"
    INFRASTRUCTURE = "infrastructure"
    OTHER = "other"
