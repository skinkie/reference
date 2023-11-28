from dataclasses import dataclass, field
from typing import Optional
from netex.accessibility_limitations_rel_structure import AccessibilityLimitationsRelStructure
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.limitation_status_enumeration import LimitationStatusEnumeration
from netex.multilingual_string import MultilingualString
from netex.suitabilities_rel_structure import SuitabilitiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityAssessmentVersionedChildStructure(VersionedChildStructure):
    """
    Type for ACCESSIBILITY ASSESSMENT.

    :ivar mobility_impaired_access: Summary indication as to whether the
        component is considered to be accessible or not.
    :ivar limitations: The ACCESSIBILITY LIMITATION that apply to
        component.
    :ivar suitabilities: The SUITABILITY of the component to meet
        specific user needs.
    :ivar comment: Comment on accessibility.
    """
    class Meta:
        name = "AccessibilityAssessment_VersionedChildStructure"

    mobility_impaired_access: LimitationStatusEnumeration = field(
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    limitations: Optional[AccessibilityLimitationsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitabilities: Optional[SuitabilitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
