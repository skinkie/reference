from dataclasses import dataclass
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OtherPlaceEquipment(PlaceEquipmentVersionStructure):
    """
    Equipment that may be in a fixed within a SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
