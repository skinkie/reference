from dataclasses import dataclass, field
from typing import List
from netex.accommodation_facility_enumeration import AccommodationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationFacilityList:
    """
    List of ACCOMMODATION FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccommodationFacilityEnumeration] = field(
        default_factory=lambda: [
            AccommodationFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        }
    )
