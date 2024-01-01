from dataclasses import dataclass, field
from typing import List
from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityInfoFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessibilityInfoFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
