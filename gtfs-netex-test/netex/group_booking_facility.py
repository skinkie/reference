from dataclasses import dataclass, field

from .group_booking_enumeration import GroupBookingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupBookingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: GroupBookingEnumeration = field(
        default=GroupBookingEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
