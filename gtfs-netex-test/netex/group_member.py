from dataclasses import dataclass
from netex.group_member_versioned_child_structure import GroupMemberVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupMember(GroupMemberVersionedChildStructure):
    """
    General purpose member of a GROUP OF ENTITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
