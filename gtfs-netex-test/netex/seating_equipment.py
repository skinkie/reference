from dataclasses import dataclass, field
from netex.seating_equipment_version_structure import SeatingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeatingEquipment(SeatingEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT describing the properties of seating.

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
