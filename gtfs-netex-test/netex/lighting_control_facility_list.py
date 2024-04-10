from dataclasses import dataclass, field
from typing import List

from .lighting_control_facility_enumeration import LightingControlFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LightingControlFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LightingControlFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
