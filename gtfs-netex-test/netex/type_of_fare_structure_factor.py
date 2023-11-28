from dataclasses import dataclass, field
from netex.type_of_fare_structure_factor_version_structure import TypeOfFareStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareStructureFactor(TypeOfFareStructureFactorVersionStructure):
    """
    A classification of FARE STRUCTURE FACTORs expressing their general
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
