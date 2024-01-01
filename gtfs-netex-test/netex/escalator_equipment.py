from dataclasses import dataclass
from .escalator_equipment_version_structure import (
    EscalatorEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EscalatorEquipment(EscalatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
