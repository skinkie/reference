from dataclasses import dataclass

from .trolley_stand_equipment_version_structure import TrolleyStandEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrolleyStandEquipment(TrolleyStandEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
