from dataclasses import dataclass
from netex.equipment_position_ref_structure import EquipmentPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPositionRef(EquipmentPositionRefStructure):
    """
    Reference to an EQUIPMENT POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
