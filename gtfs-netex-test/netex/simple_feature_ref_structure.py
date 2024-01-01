from dataclasses import dataclass
from .group_of_points_ref_structure import GroupOfPointsRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleFeatureRefStructure(GroupOfPointsRefStructure):
    pass
