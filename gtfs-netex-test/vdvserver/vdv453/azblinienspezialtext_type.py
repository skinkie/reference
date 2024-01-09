from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AzblinienspezialtextType:
    class Meta:
        name = "AZBLinienspezialtextType"

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
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    linientext: Optional[str] = field(
        default=None,
        metadata={
            "name": "Linientext",
            "type": "Element",
            "namespace": "",
        },
    )
    richtungs_id: str = field(
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    linienspezialtext: str = field(
        metadata={
            "name": "Linienspezialtext",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prioritaet: Optional[int] = field(
        default=None,
        metadata={
            "name": "Prioritaet",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 3,
            "total_digits": 1,
        },
    )
    sprachausgabe: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sprachausgabe",
            "type": "Element",
            "namespace": "",
        },
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
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
