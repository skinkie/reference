from dataclasses import dataclass
from netex.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPositionRefStructure(PlaceRefStructure):
    """
    Type for a reference to an EQUIPMENT POSITION.
    """
