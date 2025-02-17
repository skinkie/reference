from dataclasses import dataclass

from .sanitary_equipment_ref_structure import SanitaryEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SanitaryEquipmentRef(SanitaryEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
