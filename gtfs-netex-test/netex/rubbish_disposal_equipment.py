from dataclasses import dataclass, field
from netex.rubbish_disposal_equipment_version_structure import RubbishDisposalEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RubbishDisposalEquipment(RubbishDisposalEquipmentVersionStructure):
    """
    Equipment for Passengers relating to a Rubbish disposal.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
