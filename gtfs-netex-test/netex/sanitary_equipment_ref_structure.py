from dataclasses import dataclass
from .passenger_equipment_ref_structure import PassengerEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryEquipmentRefStructure(PassengerEquipmentRefStructure):
    value: RestrictedVar
