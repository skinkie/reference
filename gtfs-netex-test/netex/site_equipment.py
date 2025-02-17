from dataclasses import dataclass

from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteEquipment(SiteEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
