from dataclasses import dataclass, field
from netex.reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceReservationFacility:
    """Classification of RESERVATION FACILITY type - UIC 7037 Code list."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservationEnumeration = field(
        default=ReservationEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
