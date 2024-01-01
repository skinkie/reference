from dataclasses import dataclass, field
from typing import List
from .accessibility_tool_enumeration import AccessibilityToolEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityToolList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
