from dataclasses import dataclass

from .installed_equipment_ref_structure import InstalledEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleReleaseEquipmentRefStructure(InstalledEquipmentRefStructure):
    pass
