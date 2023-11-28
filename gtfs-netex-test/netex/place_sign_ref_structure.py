from dataclasses import dataclass
from netex.place_equipment_ref_structure import PlaceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceSignRefStructure(PlaceEquipmentRefStructure):
    """
    Type for a reference to an PLACE SIGN.
    """
