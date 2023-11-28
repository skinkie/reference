from dataclasses import dataclass
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a SITE EQUIPMENT.
    """
    class Meta:
        name = "SiteEquipment_VersionStructure"
