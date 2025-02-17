from dataclasses import dataclass, field

from .booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BookingProcessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
