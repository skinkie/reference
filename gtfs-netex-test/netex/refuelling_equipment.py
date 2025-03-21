from dataclasses import dataclass

from .refuelling_equipment_version_structure import RefuellingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RefuellingEquipment(RefuellingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
