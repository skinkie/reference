from dataclasses import dataclass, field
from typing import List
from netex.point_of_interest_classification_hierarchy_member_structure import PointOfInterestClassificationHierarchyMemberStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationHierarchyMembersRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of POINT OF INTEREST CLASSIFICATION HIERARCHY MEMBERs.
    """
    class Meta:
        name = "pointOfInterestClassificationHierarchyMembers_RelStructure"

    classification_hierarchy_member: List[PointOfInterestClassificationHierarchyMemberStructure] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationHierarchyMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
