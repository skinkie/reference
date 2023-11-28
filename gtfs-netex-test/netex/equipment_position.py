from dataclasses import dataclass, field
from netex.equipment_position_structure import EquipmentPositionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPosition(EquipmentPositionStructure):
    """
    The precise position within an EQUIPMENT PLACE where particular EQUIPMENT is
    placed.

    :ivar id: Identifier of  EQUIPMENT POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
