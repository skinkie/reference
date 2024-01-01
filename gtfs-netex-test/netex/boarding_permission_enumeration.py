from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BoardingPermissionEnumeration(Enum):
    NORMAL = "normal"
    EARLY_BOARDING_POSSIBLE_BEFORE_DEPARTURE = (
        "earlyBoardingPossibleBeforeDeparture"
    )
    LATE_ALIGHTING_POSSIBLE_AFTER_ARRIVAL = "lateAlightingPossibleAfterArrival"
    OVERNIGHT_STAY_ONBOARD_ALLOWED = "overnightStayOnboardAllowed"
