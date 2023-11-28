from dataclasses import dataclass, field
from netex.type_of_fleet_value_structure import TypeOfFleetValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFleet(TypeOfFleetValueStructure):
    """A classification for a FLEET of VEHICLEs.

    +v1.2.2

    :ivar id: Identifier of TYPE OF FLEET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
