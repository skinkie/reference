from dataclasses import dataclass

from .access_equipment_ref_structure import AccessEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class QueueingEquipmentRef(AccessEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
