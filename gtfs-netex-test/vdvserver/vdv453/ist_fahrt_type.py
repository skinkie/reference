from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .besetztgrad_type import BesetztgradType
from .fahrt_ref_type import FahrtRefType
from .ist_halt_type import IstHaltType
from .prognose_ungenau_type import PrognoseUngenauType
from .service_attribut_type import ServiceAttributType


@dataclass(kw_only=True)
class IstFahrtType:
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
    fahrt_ref: FahrtRefType = field(
        metadata={
            "name": "FahrtRef",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    komplettfahrt: bool = field(
        metadata={
            "name": "Komplettfahrt",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    umlauf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmlaufID",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_halt: List[IstHaltType] = field(
        default_factory=list,
        metadata={
            "name": "IstHalt",
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
    prognose_ungenau: Optional[PrognoseUngenauType] = field(
        default=None,
        metadata={
            "name": "PrognoseUngenau",
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
    besetztgrad: Optional[BesetztgradType] = field(
        default=None,
        metadata={
            "name": "Besetztgrad",
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
    zst: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Zst",
            "type": "Attribute",
        },
    )
