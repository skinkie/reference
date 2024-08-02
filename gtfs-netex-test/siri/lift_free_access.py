from dataclasses import dataclass

from .accessibility_structure import AccessibilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class LiftFreeAccess(AccessibilityStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"
