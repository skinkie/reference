from dataclasses import dataclass, field
from netex.trolley_stand_equipment_version_structure import TrolleyStandEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrolleyStandEquipment(TrolleyStandEquipmentVersionStructure):
    """
    Specialisation of SITE EQUIPMENT for TROLLEY STANDs.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
