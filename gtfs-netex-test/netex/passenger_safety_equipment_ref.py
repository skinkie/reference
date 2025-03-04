from dataclasses import dataclass

from .passenger_safety_equipment_ref_structure import PassengerSafetyEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerSafetyEquipmentRef(PassengerSafetyEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
