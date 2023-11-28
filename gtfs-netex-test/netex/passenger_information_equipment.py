from dataclasses import dataclass, field
from netex.passenger_information_equipment_version_structure import PassengerInformationEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerInformationEquipment(PassengerInformationEquipmentVersionStructure):
    """
    A public transport information facility, as for instance terminals (on street,
    at information desks, telematic, ...) or printed material (leaflets displayed
    at stops, booklets, ...).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
