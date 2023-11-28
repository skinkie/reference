from dataclasses import dataclass
from netex.purpose_of_equipment_profile_ref_structure import PurposeOfEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposeOfEquipmentProfileRef(PurposeOfEquipmentProfileRefStructure):
    """
    Reference to a PURPOSE OF EQUIPMENT PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
