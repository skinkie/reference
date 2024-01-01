from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SamePeriodEnumeration(Enum):
    ANY = "any"
    SAME_PERIOD = "samePeriod"
    WITHIN_SAME_PERIOD = "withinSamePeriod"
    SAME_DAY = "sameDay"
    SAME_DAY_OF_RETURN = "sameDayOfReturn"
    SAME_FARE_DAY = "sameFareDay"
    NEXT_DAY = "nextDay"
    DIFFERENT = "different"
