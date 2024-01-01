from dataclasses import dataclass
from .waiting_room_equipment_version_structure import (
    WaitingRoomEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingRoomEquipment(WaitingRoomEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
