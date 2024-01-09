from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class DatenAbrufenAnfrageType:
    datensatz_alle: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DatensatzAlle",
            "type": "Element",
            "namespace": "",
        },
    )
    sender: str = field(
        metadata={
            "name": "Sender",
            "type": "Attribute",
            "required": True,
        }
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )
