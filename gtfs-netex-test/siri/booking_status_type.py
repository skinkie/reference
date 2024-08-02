from dataclasses import dataclass, field

from .booking_status_enumeration import BookingStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class BookingStatusType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BookingStatusEnumeration = field(
        default=BookingStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
