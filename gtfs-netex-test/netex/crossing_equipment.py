from dataclasses import dataclass

from .crossing_equipment_version_structure import CrossingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrossingEquipment(CrossingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
