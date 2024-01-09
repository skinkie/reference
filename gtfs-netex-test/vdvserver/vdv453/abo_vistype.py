from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AboVistype:
    class Meta:
        name = "AboVISType"

    visid: str = field(
        metadata={
            "name": "VISID",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    linien_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
        },
    )
    richtungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
        },
    )
    zyklus: int = field(
        metadata={
            "name": "Zyklus",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    abo_id: int = field(
        metadata={
            "name": "AboID",
            "type": "Attribute",
            "required": True,
        }
    )
    verfall_zst: XmlDateTime = field(
        metadata={
            "name": "VerfallZst",
            "type": "Attribute",
            "required": True,
        }
    )
