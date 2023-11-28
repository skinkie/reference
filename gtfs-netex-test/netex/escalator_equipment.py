from dataclasses import dataclass, field
from netex.escalator_equipment_version_structure import EscalatorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EscalatorEquipment(EscalatorEquipmentVersionStructure):
    """
    Specialisation of STAIR EQUIPMENT for ESCALATORs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
