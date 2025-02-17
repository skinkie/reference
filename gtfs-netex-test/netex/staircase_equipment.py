from dataclasses import dataclass

from .staircase_equipment_version_structure import StaircaseEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StaircaseEquipment(StaircaseEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
