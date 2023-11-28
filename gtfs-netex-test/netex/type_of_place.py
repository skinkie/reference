from dataclasses import dataclass, field
from netex.type_of_place_value_structure import TypeOfPlaceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPlace(TypeOfPlaceValueStructure):
    """
    Classification of a PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
