from dataclasses import dataclass, field
from typing import List
from netex.schematic_map_member_versioned_child_structure import SchematicMapMemberVersionedChildStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMapMembersRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of SCHEMATIC MAP.

    :ivar schematic_map_member: An element linked to a SCHEMATIC MAP
        MEMBER.
    """
    class Meta:
        name = "schematicMapMembers_RelStructure"

    schematic_map_member: List[SchematicMapMemberVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMapMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
