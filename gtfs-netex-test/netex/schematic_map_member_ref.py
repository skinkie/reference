from dataclasses import dataclass
from .schematic_map_member_ref_structure import SchematicMapMemberRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapMemberRef(SchematicMapMemberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
