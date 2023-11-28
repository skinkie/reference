from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.object_refs_rel_structure import ObjectRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralGroupOfEntitiesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a GENERAL GROUP OF ENTITies.

    :ivar members: Members of  GROUP OF ENTITies.
    :ivar name_of_member_class: If group is homogeneous, name of CLASS
        of members.
    """
    class Meta:
        name = "GeneralGroupOfEntities_VersionStructure"

    members: Optional[ObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_member_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfMemberClass",
            "type": "Attribute",
        }
    )
