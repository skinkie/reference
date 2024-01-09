from dataclasses import dataclass, field
from typing import List, Optional
from .fahrt_idtype import FahrtIdtype
from .service_attribut_type import ServiceAttributType
from .soll_halt_type import SollHaltType


@dataclass(kw_only=True)
class SollFahrtType:
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    soll_halt: List[SollHaltType] = field(
        default_factory=list,
        metadata={
            "name": "SollHalt",
            "type": "Element",
            "namespace": "",
        },
    )
    umlauf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmlaufID",
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
    produkt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProduktID",
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
    zugname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Zugname",
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
    zusatzfahrt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Zusatzfahrt",
            "type": "Element",
            "namespace": "",
        },
    )
    faellt_aus: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FaelltAus",
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
    fahrzeug_typ_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FahrzeugTypID",
            "type": "Element",
            "namespace": "",
        },
    )
    service_attribut: List[ServiceAttributType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAttribut",
            "type": "Element",
            "namespace": "",
        },
    )
