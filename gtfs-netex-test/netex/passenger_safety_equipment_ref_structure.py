from dataclasses import dataclass
from netex.passenger_equipment_ref_structure import PassengerEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerSafetyEquipmentRefStructure(PassengerEquipmentRefStructure):
    """
    Type for a reference to an PASSENGER SAFETY EQUIPMENT.
    """
