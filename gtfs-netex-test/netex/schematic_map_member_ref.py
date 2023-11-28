from dataclasses import dataclass
from netex.schematic_map_member_ref_structure import SchematicMapMemberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMapMemberRef(SchematicMapMemberRefStructure):
    """
    Reference to a SCHEMATIC MAP MEMBER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
