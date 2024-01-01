from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    DEFIBRILLATOR = "defibrillator"
    ALCOHOL_TEST = "alcoholTest"
