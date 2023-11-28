from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.timing_link_refs_rel_structure import TimingLinkRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimingLinksRelStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF TIMING LINKs.

    :ivar members: TIMING LINKs in group.
    """
    class Meta:
        name = "GroupOfTimingLinks_RelStructure"

    members: Optional[TimingLinkRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
