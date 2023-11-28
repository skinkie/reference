from dataclasses import dataclass, field
from netex.help_point_equipment_version_structure import HelpPointEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HelpPointEquipment(HelpPointEquipmentVersionStructure):
    """
    Specialisation of PASSENGER EQUIPMENT for HELP POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
