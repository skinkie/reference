from dataclasses import dataclass, field
from typing import List
from netex.sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SanitaryFacilityList:
    """
    List of SANITARY FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
