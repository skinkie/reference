from dataclasses import dataclass, field
from netex.activated_equipment_version_structure import ActivatedEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivatedEquipment(ActivatedEquipmentVersionStructure):
    """
    An EQUIPMENT activated by the passage of a vehicle at an ACTIVATION POINT or on
    an ACTIVATION LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
