from dataclasses import dataclass
from netex.passenger_information_equipment_ref_structure import PassengerInformationEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerInformationEquipmentRef(PassengerInformationEquipmentRefStructure):
    """
    Reference to a PASSENGER INFORMATION EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
