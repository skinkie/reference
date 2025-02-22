from dataclasses import dataclass

from .accessibility_assessment_ref_structure import AccessibilityAssessmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessibilityAssessmentRef(AccessibilityAssessmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
