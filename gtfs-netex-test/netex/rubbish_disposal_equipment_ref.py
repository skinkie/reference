from dataclasses import dataclass

from .rubbish_disposal_equipment_ref_structure import RubbishDisposalEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RubbishDisposalEquipmentRef(RubbishDisposalEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
