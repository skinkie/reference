from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PersonalOperationTypeEnumeration(Enum):
    OWN_CAR = "ownCar"
    PRIVATE_LIFT = "privateLift"
