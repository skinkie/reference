from dataclasses import dataclass
from netex.trolley_stand_equipment_ref_structure import TrolleyStandEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrolleyStandEquipmentRef(TrolleyStandEquipmentRefStructure):
    """
    Identifier of an TROLLEY STAND EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
