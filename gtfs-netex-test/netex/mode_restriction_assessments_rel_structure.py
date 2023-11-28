from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.mode_restriction_assessment import ModeRestrictionAssessment
from netex.mode_restriction_assessment_ref import ModeRestrictionAssessmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRestrictionAssessmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of MODE RESTRICTION ASSESSMENT.
    """
    class Meta:
        name = "modeRestrictionAssessments_RelStructure"

    mode_restriction_assessment_ref_or_mode_restriction_assessment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ModeRestrictionAssessmentRef",
                    "type": ModeRestrictionAssessmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModeRestrictionAssessment",
                    "type": ModeRestrictionAssessment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
