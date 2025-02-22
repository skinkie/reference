from dataclasses import dataclass

from .waiting_room_equipment_version_structure import WaitingRoomEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WaitingRoomEquipment(WaitingRoomEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
