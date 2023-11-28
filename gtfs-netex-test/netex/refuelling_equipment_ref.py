from dataclasses import dataclass
from netex.refuelling_equipment_ref_structure import RefuellingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RefuellingEquipmentRef(RefuellingEquipmentRefStructure):
    """Identifier of an REFUELLING EQUIPMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
