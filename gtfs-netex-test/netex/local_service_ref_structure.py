from dataclasses import dataclass
from .equipment_ref_structure import EquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalServiceRefStructure(EquipmentRefStructure):
    value: RestrictedVar
