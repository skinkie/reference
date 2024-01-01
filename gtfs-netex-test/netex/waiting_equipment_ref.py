from dataclasses import dataclass
from .waiting_equipment_ref_structure import WaitingEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingEquipmentRef(WaitingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
