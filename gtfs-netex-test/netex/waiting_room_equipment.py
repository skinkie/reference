from dataclasses import dataclass, field
from netex.waiting_room_equipment_version_structure import WaitingRoomEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WaitingRoomEquipment(WaitingRoomEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT for WAITING ROOMs, classified by TYPE OF
    WAITING ROOM.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
