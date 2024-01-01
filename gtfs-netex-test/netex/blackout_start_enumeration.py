from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BlackoutStartEnumeration(Enum):
    MAY_TRAVEL_ANYTIME = "mayTravelAnytime"
    NO_TRAVEL_WITHIN_PERIOD = "noTravelWithinPeriod"
    NO_TRAVEL_WITHIN_TIMEBAND = "noTravelWithinTimeband"
    MAY_COMPLETE_IF_STARTED_BEFORE = "mayCompleteIfStartedBefore"
