from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.point_refs_rel_structure import PointRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfPointsVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF POINTs.

    :ivar members: POINTs in GROUP OF POINTs.
    """
    class Meta:
        name = "GroupOfPoints_VersionStructure"

    members: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
