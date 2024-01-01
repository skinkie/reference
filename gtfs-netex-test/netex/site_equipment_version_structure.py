from dataclasses import dataclass
from .place_equipment_version_structure import PlaceEquipmentVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "SiteEquipment_VersionStructure"
