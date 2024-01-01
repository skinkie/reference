from dataclasses import dataclass
from .help_point_equipment_ref_structure import HelpPointEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HelpPointEquipmentRef(HelpPointEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
