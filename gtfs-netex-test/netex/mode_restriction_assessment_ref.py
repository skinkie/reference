from dataclasses import dataclass
from netex.mode_restriction_assessment_ref_structure import ModeRestrictionAssessmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRestrictionAssessmentRef(ModeRestrictionAssessmentRefStructure):
    """Reference to MODE RESTRICTION ASSESSMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
