from dataclasses import dataclass, field
from netex.sanitary_equipment_version_structure import SanitaryEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SanitaryEquipment(SanitaryEquipmentVersionStructure):
    """
    A SANITARY FACILITY , e.g. WC, Shower, baby change.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
