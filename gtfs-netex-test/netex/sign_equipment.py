from dataclasses import dataclass

from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SignEquipment(SignEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
