from dataclasses import dataclass, field
from typing import Optional

from .accessibility_assessment_structure import AccessibilityAssessmentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedStopPlaceElementStructure:
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
