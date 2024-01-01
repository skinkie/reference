from dataclasses import dataclass
from .group_of_points_version_structure import GroupOfPointsVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPoints(GroupOfPointsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
