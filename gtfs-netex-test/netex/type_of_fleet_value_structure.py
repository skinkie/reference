from dataclasses import dataclass
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFleetValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF FLEET.
    """
    class Meta:
        name = "TypeOfFleet_ValueStructure"
