from dataclasses import dataclass
from .travelator_equipment_ref_structure import TravelatorEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelatorEquipmentRef(TravelatorEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
