from dataclasses import dataclass, field
from typing import List
from netex.hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HireFacilityList:
    """
    List of Hire FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
