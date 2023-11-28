from dataclasses import dataclass
from netex.installed_equipment_ref_structure import InstalledEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerEquipmentRefStructure(InstalledEquipmentRefStructure):
    """
    Type for a reference to a PASSENGER EQUIPMENT.
    """
