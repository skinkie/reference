from dataclasses import dataclass, field

from .accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessibilityTool:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityToolEnumeration = field(
        metadata={
            "required": True,
        }
    )
