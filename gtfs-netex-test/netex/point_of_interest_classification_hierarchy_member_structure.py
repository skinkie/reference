from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.point_of_interest_classification_ref_structure import PointOfInterestClassificationRefStructure
from netex.point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationHierarchyMemberStructure(VersionedChildStructure):
    """
    Type for POINT OF INTEREST CLASSIFICATION HIERARCHY MEMBER.

    :ivar point_of_interest_hierarchy_ref:
    :ivar parent_classification_ref: Parent POINT OF INTEREST
        CLASSIFICATION for this CLASSIFICATION HIERARCHY member.
    :ivar point_of_interest_classification_ref: POINT OF INTEREST
        CLASSIFICATION that is in this classification Hierarchy.
    """
    point_of_interest_hierarchy_ref: Optional[PointOfInterestHierarchyRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestHierarchyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_classification_ref: PointOfInterestClassificationRefStructure = field(
        metadata={
            "name": "ParentClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    point_of_interest_classification_ref: PointOfInterestClassificationRefStructure = field(
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
