from dataclasses import dataclass
from .trolley_stand_equipment_version_structure import (
    TrolleyStandEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrolleyStandEquipment(TrolleyStandEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
