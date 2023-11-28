from dataclasses import dataclass, field
from netex.lift_equipment_version_structure import LiftEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LiftEquipment(LiftEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for LIFTs (provides lift
    characteristics like depth, maximum load, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
