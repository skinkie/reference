from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SafetyFacilityEnumeration(Enum):
    """
    Allowed values for SAFETY Facility.
    """
    CC_TV = "ccTv"
    MOBILE_COVERAGE = "mobileCoverage"
    SOS_POINTS = "sosPoints"
    STAFFED = "staffed"
