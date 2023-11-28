from dataclasses import dataclass, field
from netex.type_of_fare_structure_element_version_structure import TypeOfFareStructureElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareStructureElement(TypeOfFareStructureElementVersionStructure):
    """
    A classification of FARE STRUCTURE ELEMENTs expressing their general
    functionalities .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
