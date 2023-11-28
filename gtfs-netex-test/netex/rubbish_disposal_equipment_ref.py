from dataclasses import dataclass
from netex.rubbish_disposal_equipment_ref_structure import RubbishDisposalEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RubbishDisposalEquipmentRef(RubbishDisposalEquipmentRefStructure):
    """
    Identifier of an RUBBISH DISPOSAL EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
