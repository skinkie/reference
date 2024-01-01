from dataclasses import dataclass
from .schematic_map_version_structure import SchematicMapVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMap(SchematicMapVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
