from dataclasses import dataclass

from .staircase_equipment_ref_structure import StaircaseEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StaircaseEquipmentRef(StaircaseEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
