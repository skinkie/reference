from dataclasses import dataclass
from netex.waiting_equipment_ref_structure import WaitingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WaitingEquipmentRef(WaitingEquipmentRefStructure):
    """
    Identifier of an WAITING EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
