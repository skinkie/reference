from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime
from .ergebnis_type import ErgebnisType


@dataclass(kw_only=True)
class StatusType:
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )
    ergebnis: ErgebnisType = field(
        metadata={
            "name": "Ergebnis",
            "type": "Attribute",
            "required": True,
        }
    )
