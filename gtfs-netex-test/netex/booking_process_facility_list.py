from dataclasses import dataclass, field
from typing import List
from netex.booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BookingProcessFacilityList:
    """
    List of BOOKING PROCESS FACILITies UIC 7037 Code list.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
