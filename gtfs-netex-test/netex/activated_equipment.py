from dataclasses import dataclass

from .activated_equipment_version_structure import ActivatedEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipment(ActivatedEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
