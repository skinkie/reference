from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class ZurueckhaltungBisType:
    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )
    fahrzeug_quittung: bool = field(
        default=True,
        metadata={
            "name": "FahrzeugQuittung",
            "type": "Attribute",
        },
    )
