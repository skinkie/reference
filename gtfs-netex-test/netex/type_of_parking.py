from dataclasses import dataclass, field
from netex.type_of_parking_value_structure import TypeOfParkingValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfParking(TypeOfParkingValueStructure):
    """A classification for a PARKING.

    +v1.2.2

    :ivar id: Identifier of TYPE OF PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
