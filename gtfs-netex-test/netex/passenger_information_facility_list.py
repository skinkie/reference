from dataclasses import dataclass, field
from typing import List
from netex.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerInformationFacilityList:
    """
    List of PASSENGER INFO FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
