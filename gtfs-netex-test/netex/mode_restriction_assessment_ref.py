from dataclasses import dataclass

from .mode_restriction_assessment_ref_structure import ModeRestrictionAssessmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRestrictionAssessmentRef(ModeRestrictionAssessmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
