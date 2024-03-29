from dataclasses import dataclass, field
from typing import List

from .catering_facility_enumeration import CateringFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CateringFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
