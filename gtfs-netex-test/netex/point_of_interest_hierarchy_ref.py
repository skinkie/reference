from dataclasses import dataclass

from .point_of_interest_hierarchy_ref_structure import PointOfInterestHierarchyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestHierarchyRef(PointOfInterestHierarchyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
