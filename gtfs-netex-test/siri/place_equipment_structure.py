from dataclasses import dataclass, field
from typing import Optional

from .extensions_2 import Extensions2
from .installed_equipment_structure import InstalledEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class PlaceEquipmentStructure(InstalledEquipmentStructure):
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
