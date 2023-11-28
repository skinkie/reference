from dataclasses import dataclass, field
from netex.ramp_equipment_version_structure import RampEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RampEquipment(RampEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for ramps (provides ramp
    characteristics like length, gradient, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
