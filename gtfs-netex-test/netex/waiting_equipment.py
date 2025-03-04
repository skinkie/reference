from dataclasses import dataclass

from .waiting_equipment_version_structure import WaitingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WaitingEquipment(WaitingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
