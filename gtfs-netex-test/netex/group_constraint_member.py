from dataclasses import dataclass
from netex.group_constraint_member_versioned_child_structure import GroupConstraintMemberVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupConstraintMember(GroupConstraintMemberVersionedChildStructure):
    """
    Specifies a member of a set.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
