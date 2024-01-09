from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .linien_filter_type import LinienFilterType


@dataclass(kw_only=True)
class AboAustype:
    class Meta:
        name = "AboAUSType"

    linien_filter: List[LinienFilterType] = field(
        default_factory=list,
        metadata={
            "name": "LinienFilter",
            "type": "Element",
            "namespace": "",
        },
    )
    umlauf_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UmlaufID",
            "type": "Element",
            "namespace": "",
        },
    )
    hysterese: int = field(
        metadata={
            "name": "Hysterese",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vorschauzeit: int = field(
        metadata={
            "name": "Vorschauzeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mit_ges_anschluss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MitGesAnschluss",
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
