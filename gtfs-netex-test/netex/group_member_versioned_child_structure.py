from dataclasses import dataclass, field
from typing import Optional
from netex.abstract_group_member_versioned_child_structure import AbstractGroupMemberVersionedChildStructure
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupMemberVersionedChildStructure(AbstractGroupMemberVersionedChildStructure):
    """
    Type for a General purpose member of a GROUP OF ENTITies.

    :ivar group_ref: Parent GROUP OF ENTITies to which this member
        assigns service  -  If given by context, can be omitted.
    :ivar member_object_ref: Reference to a member of the group.
    """
    class Meta:
        name = "GroupMember_VersionedChildStructure"

    group_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    member_object_ref: VersionOfObjectRefStructure = field(
        metadata={
            "name": "MemberObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
