from dataclasses import dataclass, field
from typing import List
from netex.reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReservedSpaceFacilityList:
    """
    List of RESERVED SPACE FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservedSpaceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
