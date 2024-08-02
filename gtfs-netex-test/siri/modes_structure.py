from dataclasses import dataclass, field
from typing import List

from .all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ModesStructure:
    mode: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    exclude: bool = field(
        default=False,
        metadata={
            "name": "Exclude",
            "type": "Attribute",
        },
    )
