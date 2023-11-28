from dataclasses import dataclass, field
from typing import List
from netex.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCommsFacilityList:
    """
    List of PASSENGER COMMS FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
