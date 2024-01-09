from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class LinienFilterType:
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    richtungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
        },
    )
