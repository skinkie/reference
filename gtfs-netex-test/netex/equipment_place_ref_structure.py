from dataclasses import dataclass

from .place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EquipmentPlaceRefStructure(PlaceRefStructure):
    pass
