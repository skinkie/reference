from dataclasses import dataclass

from .passenger_information_equipment_version_structure import PassengerInformationEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationEquipment(PassengerInformationEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
