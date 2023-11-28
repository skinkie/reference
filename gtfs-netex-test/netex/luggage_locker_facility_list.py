from dataclasses import dataclass, field
from typing import List
from netex.luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageLockerFacilityList:
    """
    List of LUGGAGE LOCKER FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
