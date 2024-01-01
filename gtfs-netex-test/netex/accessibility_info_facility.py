from dataclasses import dataclass, field
from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityInfoFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityInfoFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
