from dataclasses import dataclass, field
from netex.queueing_equipment_version_structure import QueueingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QueueingEquipment(QueueingEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT dedicated to queuing.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
