from dataclasses import dataclass, field
from typing import List
from netex.mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityFacilityList:
    """
    List of MOBILITY FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
