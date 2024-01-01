from dataclasses import dataclass
from .site_equipment_ref_structure import SiteEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingEquipmentRefStructure(SiteEquipmentRefStructure):
    value: RestrictedVar
