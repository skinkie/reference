from dataclasses import dataclass

from .spot_equipment_version_structure import SpotEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotEquipment1(SpotEquipmentVersionStructure):
    class Meta:
        name = "SpotEquipment"
        namespace = "http://www.netex.org.uk/netex"
