from dataclasses import dataclass, field
from netex.refuelling_equipment_version_structure import RefuellingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RefuellingEquipment(RefuellingEquipmentVersionStructure):
    """Specialisation of PLACE EQUIPMENT for REFUELLING.

    +v1.2.2

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
