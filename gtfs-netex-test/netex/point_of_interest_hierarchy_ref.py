from dataclasses import dataclass
from .point_of_interest_hierarchy_ref_structure import (
    PointOfInterestHierarchyRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestHierarchyRef(PointOfInterestHierarchyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
