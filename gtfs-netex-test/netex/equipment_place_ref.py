from dataclasses import dataclass
from netex.equipment_place_ref_structure import EquipmentPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPlaceRef(EquipmentPlaceRefStructure):
    """
    Reference to an EQUIPMENT PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
