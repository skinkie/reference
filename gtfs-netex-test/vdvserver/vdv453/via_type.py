from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class ViaType:
    haltestellen_name: str = field(
        metadata={
            "name": "HaltestellenName",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    haltestellen_prioritaet: Optional[int] = field(
        default=None,
        metadata={
            "name": "HaltestellenPrioritaet",
            "type": "Element",
            "namespace": "",
        },
    )
