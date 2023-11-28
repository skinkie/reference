from dataclasses import dataclass, field
from netex.accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityTool:
    """
    Classification of ACCESSIBILITY TOOLs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityToolEnumeration = field(
        metadata={
            "required": True,
        }
    )
