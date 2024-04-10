from dataclasses import dataclass

from .access_equipment_ref_structure import AccessEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEquipmentRef(AccessEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
