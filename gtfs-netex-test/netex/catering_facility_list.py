from dataclasses import dataclass, field
from typing import List
from netex.catering_facility_enumeration import CateringFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CateringFacilityList:
    """
    List of CATERING FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CateringFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
