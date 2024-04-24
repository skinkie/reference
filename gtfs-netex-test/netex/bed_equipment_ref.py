from dataclasses import dataclass

from .bed_equipment_ref_structure import BedEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BedEquipmentRef(BedEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
