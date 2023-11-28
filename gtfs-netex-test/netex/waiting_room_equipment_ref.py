from dataclasses import dataclass
from netex.waiting_room_equipment_ref_structure import WaitingRoomEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WaitingRoomEquipmentRef(WaitingRoomEquipmentRefStructure):
    """
    Identifier of an WAITING ROOM EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
