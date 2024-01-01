from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelBillingPolicyEnumeration(Enum):
    BILL_AS_YOU_GO = "billAsYouGo"
    BILL_ON_THRESHOLD = "billOnThreshold"
    BILL_AT_FARE_DAY_END = "billAtFareDayEnd"
    BILL_AT_PERIOD_END = "billAtPeriodEnd"
