from dataclasses import dataclass

from .bed_equipment_version_structure import BedEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BedEquipment(BedEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
