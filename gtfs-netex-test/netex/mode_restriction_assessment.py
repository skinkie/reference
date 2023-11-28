from dataclasses import dataclass, field
from netex.mode_restriction_assessment_version_structure import ModeRestrictionAssessmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRestrictionAssessment(ModeRestrictionAssessmentVersionStructure):
    """
    Qualification of a ROUTE LINK resulting from the analysis of restrictions
    concerning the related INFRASTRUCTURE LINKs  +v1.2.2.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
