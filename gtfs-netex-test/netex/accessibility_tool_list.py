from dataclasses import dataclass, field
from typing import List
from netex.accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityToolList:
    """
    List of ACCESSIBILITY TOOLs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
