from dataclasses import dataclass, field
from typing import List
from netex.nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NuisanceFacilityList:
    """
    List of NUISANCE FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
