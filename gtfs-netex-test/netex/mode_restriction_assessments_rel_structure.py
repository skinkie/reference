from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .mode_restriction_assessment import ModeRestrictionAssessment
from .mode_restriction_assessment_ref import ModeRestrictionAssessmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ModeRestrictionAssessmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "modeRestrictionAssessments_RelStructure"

    mode_restriction_assessment_ref_or_mode_restriction_assessment: list[Union[ModeRestrictionAssessmentRef, ModeRestrictionAssessment]] = field(
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
        },
    )
