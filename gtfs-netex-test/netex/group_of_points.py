from dataclasses import dataclass, field
from netex.group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfPoints(GroupOfPointsVersionStructure):
    """
    A grouping of POINTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
