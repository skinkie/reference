from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SafetyFacilityEnumeration(Enum):
    CC_TV = "ccTv"
    MOBILE_COVERAGE = "mobileCoverage"
    SOS_POINTS = "sosPoints"
    STAFFED = "staffed"
