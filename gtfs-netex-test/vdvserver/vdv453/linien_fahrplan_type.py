from dataclasses import dataclass, field
from typing import List, Optional
from .soll_fahrt_type import SollFahrtType


@dataclass(kw_only=True)
class LinienFahrplanType:
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    richtungs_id: str = field(
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fahrplan_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FahrplanVersionID",
            "type": "Element",
            "namespace": "",
        },
    )
    soll_fahrt: List[SollFahrtType] = field(
        default_factory=list,
        metadata={
            "name": "SollFahrt",
            "type": "Element",
            "namespace": "",
        },
    )
    produkt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProduktID",
            "type": "Element",
            "namespace": "",
        },
    )
    linien_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinienText",
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
    von_richtungs_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "VonRichtungsText",
            "type": "Element",
            "namespace": "",
        },
    )
    verkehrsmittel_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "VerkehrsmittelText",
            "type": "Element",
            "namespace": "",
        },
    )
    prognose_moeglich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrognoseMoeglich",
            "type": "Element",
            "namespace": "",
        },
    )
    fahrrad_mitnahme: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FahrradMitnahme",
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
