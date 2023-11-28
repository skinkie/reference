from dataclasses import dataclass
from netex.site_equipment_ref_structure import SiteEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WaitingEquipmentRefStructure(SiteEquipmentRefStructure):
    """
    Type for a reference to an WAITING EQUIPMENT.
    """
