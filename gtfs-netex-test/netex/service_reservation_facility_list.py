from dataclasses import dataclass, field
from typing import List
from netex.reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceReservationFacilityList:
    """
    List of RESERVATION FACILITies UIC 7037 Code list.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
