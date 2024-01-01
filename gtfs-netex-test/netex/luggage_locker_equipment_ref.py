from dataclasses import dataclass
from .luggage_locker_equipment_ref_structure import (
    LuggageLockerEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerEquipmentRef(LuggageLockerEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
