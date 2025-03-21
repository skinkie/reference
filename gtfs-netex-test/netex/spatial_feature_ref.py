from dataclasses import dataclass

from .group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpatialFeatureRef(GroupOfPointsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
