from dataclasses import dataclass, field
from netex.point_of_interest_classification_hierarchy_version_structure import PointOfInterestClassificationHierarchyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationHierarchy(PointOfInterestClassificationHierarchyVersionStructure):
    """A logical hierarchy for organizing POINT OF INTEREST CLASSIFICATIONs.

    A POINT OF INTEREST CLASSIFICATION can belong to more than one
    hierarchy.

    :ivar id: Identifier of POINT OF INTEREST  HIERARCHY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
