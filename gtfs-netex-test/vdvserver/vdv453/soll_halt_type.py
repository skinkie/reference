from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .soll_anschluss_type import SollAnschlussType


@dataclass(kw_only=True)
class SollHaltType:
    halt_id: str = field(
        metadata={
            "name": "HaltID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    haltestellen_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "HaltestellenName",
            "type": "Element",
            "namespace": "",
        },
    )
    abfahrtszeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Abfahrtszeit",
            "type": "Element",
            "namespace": "",
        },
    )
    ankunftszeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Ankunftszeit",
            "type": "Element",
            "namespace": "",
        },
    )
    abfahrtssteig_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "AbfahrtssteigText",
            "type": "Element",
            "namespace": "",
        },
    )
    ankunftssteig_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnkunftssteigText",
            "type": "Element",
            "namespace": "",
        },
    )
    einsteigeverbot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Einsteigeverbot",
            "type": "Element",
            "namespace": "",
        },
    )
    aussteigeverbot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Aussteigeverbot",
            "type": "Element",
            "namespace": "",
        },
    )
    durchfahrt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Durchfahrt",
            "type": "Element",
            "namespace": "",
        },
    )
    richtungs_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "RichtungsText",
            "type": "Element",
            "namespace": "",
        },
    )
    von_richtung_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "VonRichtungText",
            "type": "Element",
            "namespace": "",
        },
    )
    hinweis_text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "HinweisText",
            "type": "Element",
            "namespace": "",
        },
    )
    soll_anschluss: List[SollAnschlussType] = field(
        default_factory=list,
        metadata={
            "name": "SollAnschluss",
            "type": "Element",
            "namespace": "",
        },
    )
