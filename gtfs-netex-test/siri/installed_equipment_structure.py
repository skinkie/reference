from dataclasses import dataclass

from .abstract_equipment_structure import AbstractEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class InstalledEquipmentStructure(AbstractEquipmentStructure):
    pass
