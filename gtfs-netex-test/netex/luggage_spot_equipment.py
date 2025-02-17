from dataclasses import dataclass

from .luggage_spot_equipment_version_structure import LuggageSpotEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageSpotEquipment(LuggageSpotEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
