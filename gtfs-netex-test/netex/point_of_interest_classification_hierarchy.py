from dataclasses import dataclass

from .point_of_interest_classification_hierarchy_version_structure import PointOfInterestClassificationHierarchyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestClassificationHierarchy(PointOfInterestClassificationHierarchyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
