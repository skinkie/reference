from dataclasses import dataclass, field
from typing import Optional
from netex.accessibility_assessment_versioned_child_structure import AccessibilityAssessmentVersionedChildStructure
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessZoneVersionStructure(ZoneVersionStructure):
    """
    Type for an ACCESS ZONE.

    :ivar accessibility_assessment: Accessibility values associated with
        ACCESS ZONE.
    :ivar all_areas_wheelchair_accessible: Whether all areas of the
        ACCESS ZONE are wheelchair accessible.
    """
    class Meta:
        name = "AccessZone_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessmentVersionedChildStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
