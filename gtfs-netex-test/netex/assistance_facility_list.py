from dataclasses import dataclass, field
from typing import List
from netex.assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceFacilityList:
    """
    List of ASSISTANCE FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
