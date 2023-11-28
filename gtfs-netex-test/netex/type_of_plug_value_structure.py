from dataclasses import dataclass
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPlugValueStructure(TypeOfEntityVersionStructure):
    """Type for a TYPE OF PLUG.

    +v1.2.2
    """
    class Meta:
        name = "TypeOfPlug_ValueStructure"
