from dataclasses import dataclass

from .passenger_equipment_ref_structure import PassengerEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleEquipmentRefStructure(PassengerEquipmentRefStructure):
    pass
