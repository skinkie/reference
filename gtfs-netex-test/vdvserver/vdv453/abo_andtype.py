from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AboAndtype:
    class Meta:
        name = "AboANDType"

    kanal_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "KanalID",
            "type": "Element",
            "namespace": "",
        },
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
