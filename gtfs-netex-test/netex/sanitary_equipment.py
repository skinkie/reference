from dataclasses import dataclass

from .sanitary_equipment_version_structure import SanitaryEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SanitaryEquipment(SanitaryEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
