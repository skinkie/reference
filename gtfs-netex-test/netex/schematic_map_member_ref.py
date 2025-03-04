from dataclasses import dataclass

from .schematic_map_member_ref_structure import SchematicMapMemberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SchematicMapMemberRef(SchematicMapMemberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
