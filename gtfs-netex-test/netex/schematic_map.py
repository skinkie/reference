from dataclasses import dataclass, field
from netex.schematic_map_version_structure import SchematicMapVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMap(SchematicMapVersionStructure):
    """
    A projection of a set of ENTITies onto a bitmap image so as to support
    hyperlinked interactions.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
