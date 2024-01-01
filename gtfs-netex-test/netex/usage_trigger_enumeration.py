from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageTriggerEnumeration(Enum):
    ENROLMENT = "enrolment"
    RESERVATION = "reservation"
    PURCHASE = "purchase"
    FULFILMENT = "fulfilment"
    ACTIVATION = "activation"
    SPECIFIED_START_DATE = "specifiedStartDate"
    START_OUTBOUND_RIDE = "startOutboundRide"
    END_OUTBOUND_RIDE = "endOutboundRide"
    START_RETURN_RIDE = "startReturnRide"
    START_OF_PERIOD = "startOfPeriod"
    DAY_OFFSET_BEFORE_CALENDAR_PERIOD = "dayOffsetBeforeCalendarPeriod"
