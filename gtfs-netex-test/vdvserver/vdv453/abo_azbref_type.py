from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AboAzbrefType:
    class Meta:
        name = "AboAZBRefType"

    azbid: str = field(
        metadata={
            "name": "AZBID",
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
    frueheste_abfahrtszeit: XmlDateTime = field(
        metadata={
            "name": "FruehesteAbfahrtszeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    spaeteste_abfahrtszeit: XmlDateTime = field(
        metadata={
            "name": "SpaetesteAbfahrtszeit",
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
