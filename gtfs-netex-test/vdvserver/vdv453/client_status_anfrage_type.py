from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class ClientStatusAnfrageType:
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
    mit_abos: bool = field(
        default=False,
        metadata={
            "name": "MitAbos",
            "type": "Attribute",
        },
    )
