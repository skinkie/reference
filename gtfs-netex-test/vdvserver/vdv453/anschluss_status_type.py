from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .warte_info_type import WarteInfoType


@dataclass(kw_only=True)
class AnschlussStatusType:
    warte_info: WarteInfoType = field(
        metadata={
            "name": "WarteInfo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    abfahrtszeit_abbringer_prognose: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AbfahrtszeitAbbringerPrognose",
            "type": "Element",
            "namespace": "",
        },
    )
    sicherung_aufgehoben: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SicherungAufgehoben",
            "type": "Element",
            "namespace": "",
        },
    )
    anschluss_id: str = field(
        metadata={
            "name": "AnschlussID",
            "type": "Attribute",
            "required": True,
        }
    )
