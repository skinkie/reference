from dataclasses import dataclass, field

from .accessibility_enumeration import AccessibilityEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class AccessibilityStructure:
    value: AccessibilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
