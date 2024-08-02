from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DepartureBoardingActivityEnumeration(Enum):
    BOARDING = "boarding"
    NO_BOARDING = "noBoarding"
    PASS_THRU = "passThru"
