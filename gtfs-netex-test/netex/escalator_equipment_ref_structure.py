from dataclasses import dataclass
from .access_equipment_ref_structure import AccessEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EscalatorEquipmentRefStructure(AccessEquipmentRefStructure):
    value: RestrictedVar
