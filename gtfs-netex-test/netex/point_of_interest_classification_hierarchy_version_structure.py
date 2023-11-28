from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.point_of_interest_classification_hierarchy_members_rel_structure import PointOfInterestClassificationHierarchyMembersRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationHierarchyVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for POINT OF INTEREST CLASSIFICATION HIERARCHY.

    :ivar members: Members of the POINT OF INTEREST HIERARCHY.
    """
    class Meta:
        name = "PointOfInterestClassificationHierarchy_VersionStructure"

    members: Optional[PointOfInterestClassificationHierarchyMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
