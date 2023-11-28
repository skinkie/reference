from dataclasses import dataclass
from netex.accessibility_assessment_ref_structure import AccessibilityAssessmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityAssessmentRef(AccessibilityAssessmentRefStructure):
    """
    Reference to an ACCESSIBILITY ASSESSMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
