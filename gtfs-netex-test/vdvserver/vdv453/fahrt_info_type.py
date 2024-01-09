from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .direktruf_type import DirektrufType


@dataclass(kw_only=True)
class FahrtInfoType:
    fahrzeug_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FahrzeugID",
            "type": "Element",
            "namespace": "",
        },
    )
    linien_nr: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinienNr",
            "type": "Element",
            "namespace": "",
        },
    )
    umlauf_nr: Optional[int] = field(
        default=None,
        metadata={
            "name": "UmlaufNr",
            "type": "Element",
            "namespace": "",
        },
    )
    kurs_nr: Optional[int] = field(
        default=None,
        metadata={
            "name": "KursNr",
            "type": "Element",
            "namespace": "",
        },
    )
    start_hst_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartHstLang",
            "type": "Element",
            "namespace": "",
        },
    )
    start_hst: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartHst",
            "type": "Element",
            "namespace": "",
        },
    )
    ziel_hst_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZielHstLang",
            "type": "Element",
            "namespace": "",
        },
    )
    ziel_hst: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZielHst",
            "type": "Element",
            "namespace": "",
        },
    )
    abfahrtszeit_start_hst: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AbfahrtszeitStartHst",
            "type": "Element",
            "namespace": "",
        },
    )
    ankunftszeit_ziel_hst: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AnkunftszeitZielHst",
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
    betreiber: Optional[str] = field(
        default=None,
        metadata={
            "name": "Betreiber",
            "type": "Element",
            "namespace": "",
        },
    )
    service_merkmal: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceMerkmal",
            "type": "Element",
            "namespace": "",
        },
    )
    direktruf: Optional[DirektrufType] = field(
        default=None,
        metadata={
            "name": "Direktruf",
            "type": "Element",
            "namespace": "",
        },
    )
