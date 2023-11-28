from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelBillingPolicyEnumeration(Enum):
    """
    Allowed values for  Billing Policy.

    :cvar BILL_AS_YOU_GO: Bill for use immediately on incurring travel.
    :cvar BILL_ON_THRESHOLD: Only raise bill when threshold is reached
    :cvar BILL_AT_FARE_DAY_END: Bill at end of evey fare day.
    :cvar BILL_AT_PERIOD_END: Bill at end of a specified period.
    """
    BILL_AS_YOU_GO = "billAsYouGo"
    BILL_ON_THRESHOLD = "billOnThreshold"
    BILL_AT_FARE_DAY_END = "billAtFareDayEnd"
    BILL_AT_PERIOD_END = "billAtPeriodEnd"
