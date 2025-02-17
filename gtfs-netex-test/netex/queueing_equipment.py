from dataclasses import dataclass

from .queueing_equipment_version_structure import QueueingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class QueueingEquipment(QueueingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
