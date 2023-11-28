from dataclasses import dataclass
from netex.point_of_interest_hierarchy_ref_structure import PointOfInterestHierarchyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestHierarchyRef(PointOfInterestHierarchyRefStructure):
    """
    Classification of a POINT OF INTEREST CLASSIFICATION HIERARCHY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
