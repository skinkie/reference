from dataclasses import dataclass

from .refuelling_equipment_ref_structure import RefuellingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RefuellingEquipmentRef(RefuellingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
