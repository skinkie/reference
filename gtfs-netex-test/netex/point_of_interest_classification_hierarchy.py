from dataclasses import dataclass
from .point_of_interest_classification_hierarchy_version_structure import (
    PointOfInterestClassificationHierarchyVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestClassificationHierarchy(
    PointOfInterestClassificationHierarchyVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
