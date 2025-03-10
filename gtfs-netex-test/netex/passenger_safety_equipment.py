from dataclasses import dataclass

from .passenger_safety_equipment_version_structure import PassengerSafetyEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerSafetyEquipment(PassengerSafetyEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
