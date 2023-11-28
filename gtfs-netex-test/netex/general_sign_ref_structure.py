from dataclasses import dataclass
from netex.place_equipment_ref_structure import PlaceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralSignRefStructure(PlaceEquipmentRefStructure):
    """
    Type for a reference to an GENERAL SIGN.
    """
