from dataclasses import dataclass
from netex.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPassengerInformationEquipmentRefStructure(TypeOfValueRefStructure):
    """
    Type for a reference to a TYPE OF PASSENGER INFORMATION EQUIPMENT.
    """
