from dataclasses import dataclass

from .luggage_spot_equipment_ref_structure import LuggageSpotEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpotEquipmentRef(LuggageSpotEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
