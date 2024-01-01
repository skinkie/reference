from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FunicularSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    FUNICULAR = "funicular"
    STREET_CABLE_CAR = "streetCableCar"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    UNDEFINED_FUNICULAR = "undefinedFunicular"
