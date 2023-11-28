from dataclasses import dataclass, field
from netex.accessibility_info_facility_enumeration import AccessibilityInfoFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityInfoFacility:
    """Classification of ACCESSIBILITY INFO FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityInfoFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
