from dataclasses import dataclass
from netex.group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeatureRefStructure(GroupOfPointsRefStructure):
    """
    Type for a reference to a COMPLEX FEATURE.
    """
