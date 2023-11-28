from dataclasses import dataclass
from netex.passenger_safety_equipment_ref_structure import PassengerSafetyEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerSafetyEquipmentRef(PassengerSafetyEquipmentRefStructure):
    """
    Identifier of an PASSENGER SAFETY EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
