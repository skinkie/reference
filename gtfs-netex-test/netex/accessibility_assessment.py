from dataclasses import dataclass
from .accessibility_assessment_versioned_child_structure import (
    AccessibilityAssessmentVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityAssessment(AccessibilityAssessmentVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
