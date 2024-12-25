from dataclasses import dataclass, field

from .accessibility_assessment import AccessibilityAssessment
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityAssessmentsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "accessibilityAssessments_RelStructure"

    accessibility_assessment: list[AccessibilityAssessment] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
