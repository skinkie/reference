from dataclasses import dataclass

from .shelter_equipment_ref_structure import ShelterEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ShelterEquipmentRef(ShelterEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
