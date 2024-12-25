from dataclasses import dataclass, field

from .reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceReservationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
