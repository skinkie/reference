from dataclasses import dataclass, field
from netex.type_of_passenger_information_equipment_value_structure import TypeOfPassengerInformationEquipmentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPassengerInformationEquipment(TypeOfPassengerInformationEquipmentValueStructure):
    """
    Classification of a PASSENGER INFORMATION EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
