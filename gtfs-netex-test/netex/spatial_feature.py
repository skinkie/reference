from dataclasses import dataclass
from netex.group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpatialFeature(GroupOfPointsVersionStructure):
    """
    Abstract SPATIAL FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
