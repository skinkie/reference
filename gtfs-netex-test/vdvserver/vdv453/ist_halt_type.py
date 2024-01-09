from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .besetztgrad_type import BesetztgradType
from .prognose_ungenau_type import PrognoseUngenauType
from .zeit_qualitaet_type import ZeitQualitaetType


@dataclass(kw_only=True)
class IstHaltType:
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
    ist_abfahrt_prognose: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IstAbfahrtPrognose",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_ankunft_prognose: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IstAnkunftPrognose",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_abfahrt_prognose_qualitaet: Optional[ZeitQualitaetType] = field(
        default=None,
        metadata={
            "name": "IstAbfahrtPrognoseQualitaet",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_ankunft_prognose_qualitaet: Optional[ZeitQualitaetType] = field(
        default=None,
        metadata={
            "name": "IstAnkunftPrognoseQualitaet",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_abfahrt_disposition: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IstAbfahrtDisposition",
            "type": "Element",
            "namespace": "",
        },
    )
    ist_ankunft_disposition: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IstAnkunftDisposition",
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
    zusatzhalt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Zusatzhalt",
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
    besetztgrad: Optional[BesetztgradType] = field(
        default=None,
        metadata={
            "name": "Besetztgrad",
            "type": "Element",
            "namespace": "",
        },
    )
