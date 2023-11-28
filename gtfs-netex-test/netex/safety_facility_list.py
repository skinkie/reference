from dataclasses import dataclass, field
from typing import List
from netex.safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SafetyFacilityList:
    """
    List of SAFETY FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
