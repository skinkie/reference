from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.link_refs_rel_structure import LinkRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfLinksVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF LINKs.

    :ivar members: Links in group.
    """
    class Meta:
        name = "GroupOfLinks_VersionStructure"

    members: Optional[LinkRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
