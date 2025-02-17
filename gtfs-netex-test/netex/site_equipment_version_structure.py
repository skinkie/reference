from dataclasses import dataclass

from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "SiteEquipment_VersionStructure"
