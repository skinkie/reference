from dataclasses import dataclass
from netex.sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SignEquipment(SignEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for signs (heading signs, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
