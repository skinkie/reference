from dataclasses import dataclass
from netex.type_of_fleet_ref_structure import TypeOfFleetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFleetRef(TypeOfFleetRefStructure):
    """Reference to a TYPE OF FLEET.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
