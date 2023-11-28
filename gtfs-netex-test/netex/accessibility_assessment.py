from dataclasses import dataclass, field
from netex.accessibility_assessment_versioned_child_structure import AccessibilityAssessmentVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityAssessment(AccessibilityAssessmentVersionedChildStructure):
    """The accessibility characteristics of an entity used by passengers such as a
    STOP PLACE, or a STOP PLACE COMPONENT.

    Described by ACCESSIBILITY LIMITATIONs, and/or a set of
    SUITABILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
