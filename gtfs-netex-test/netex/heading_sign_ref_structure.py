from dataclasses import dataclass
from .place_equipment_ref_structure import PlaceEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadingSignRefStructure(PlaceEquipmentRefStructure):
    value: RestrictedVar
