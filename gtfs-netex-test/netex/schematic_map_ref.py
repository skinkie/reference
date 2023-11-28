from dataclasses import dataclass
from netex.schematic_map_ref_structure import SchematicMapRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMapRef(SchematicMapRefStructure):
    """
    Reference to a SCHEMATIC MAP.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
