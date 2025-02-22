from dataclasses import dataclass, field
from typing import Optional

from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .point_refs_rel_structure import PointRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfPointsVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfPoints_VersionStructure"

    members: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
