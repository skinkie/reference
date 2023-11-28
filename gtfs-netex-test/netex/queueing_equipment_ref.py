from dataclasses import dataclass
from netex.access_equipment_ref_structure import AccessEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QueueingEquipmentRef(AccessEquipmentRefStructure):
    """
    Identifier of an QUEUEING EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
