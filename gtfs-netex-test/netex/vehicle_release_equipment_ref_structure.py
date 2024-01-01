from dataclasses import dataclass
from .installed_equipment_ref_structure import InstalledEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleReleaseEquipmentRefStructure(InstalledEquipmentRefStructure):
    value: RestrictedVar
