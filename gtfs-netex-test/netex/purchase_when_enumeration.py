from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseWhenEnumeration(Enum):
    ADVANCE_ONLY = "advanceOnly"
    UNTIL_PREVIOUS_DAY = "untilPreviousDay"
    DAY_OF_TRAVEL_ONLY = "dayOfTravelOnly"
    ADVANCE_AND_DAY_OF_TRAVEL = "advanceAndDayOfTravel"
    TIME_OF_TRAVEL_ONLY = "timeOfTravelOnly"
    SUBSCRIPTION_CHARGE_MOMENT = "subscriptionChargeMoment"
    OTHER = "other"
