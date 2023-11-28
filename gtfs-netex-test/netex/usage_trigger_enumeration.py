from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageTriggerEnumeration(Enum):
    """
    Allowed values for Usage Trigger.

    :cvar ENROLMENT: Validity period starts when user registers (e.g.
        creates a customer account).
    :cvar RESERVATION: Validity period starts when user makes a
        reservation.
    :cvar PURCHASE: Validity period starts when user makes a purchase.
    :cvar FULFILMENT: Validity period starts when user collects their
        travel documents.
    :cvar ACTIVATION: Validity period starts when user activates a
        product.
    :cvar SPECIFIED_START_DATE: Validity period starts on date specified
        on produc..
    :cvar START_OUTBOUND_RIDE: Validity period starts on commencement of
        outbound trip.
    :cvar END_OUTBOUND_RIDE: Validity period starts on completion of
        outbound trip of a return or multi-part trip.
    :cvar START_RETURN_RIDE: Validity period starts on commencement of
        return trip.
    :cvar START_OF_PERIOD: Validity period starts at beginning of
        interval specified for product   (e.g.  every month  for a
        monthly pass that renews automatically).
    :cvar DAY_OFFSET_BEFORE_CALENDAR_PERIOD: Validity period starts a
        specifed number of days before  beginning of specified start
        date .
    """
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
