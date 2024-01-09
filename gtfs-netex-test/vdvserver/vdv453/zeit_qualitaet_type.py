from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class ZeitQualitaetType:
    prognose_verlaesslichkeit: int = field(
        metadata={
            "name": "PrognoseVerlaesslichkeit",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
            "total_digits": 1,
        }
    )
    zeit_min: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ZeitMin",
            "type": "Element",
            "namespace": "",
        },
    )
    zeit_max: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ZeitMax",
            "type": "Element",
            "namespace": "",
        },
    )
