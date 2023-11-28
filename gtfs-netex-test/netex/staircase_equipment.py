from dataclasses import dataclass, field
from netex.staircase_equipment_version_structure import StaircaseEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StaircaseEquipment(StaircaseEquipmentVersionStructure):
    """
    Specialisation of STAIR EQUIPMENT for stair cases.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
