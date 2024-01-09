from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype
from .fahrt_info_type import FahrtInfoType
from .fahrt_status_type import FahrtStatusType
from .traktions_type import TraktionsType
from .via_type import ViaType


@dataclass(kw_only=True)
class AzbfahrplanlageType:
    class Meta:
        name = "AZBFahrplanlageType"

    azbid: str = field(
        metadata={
            "name": "AZBID",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    hst_seq_zaehler: int = field(
        metadata={
            "name": "HstSeqZaehler",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    traktion: Optional[TraktionsType] = field(
        default=None,
        metadata={
            "name": "Traktion",
            "type": "Element",
            "namespace": "",
        },
    )
    betriebliche_fahrzeugnummer: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BetrieblicheFahrzeugnummer",
            "type": "Element",
            "namespace": "",
        },
    )
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    linien_text: str = field(
        metadata={
            "name": "LinienText",
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
    richtungs_text: str = field(
        metadata={
            "name": "RichtungsText",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    von_richtungs_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "VonRichtungsText",
            "type": "Element",
            "namespace": "",
        },
    )
    abmelde_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AbmeldeID",
            "type": "Element",
            "namespace": "",
        },
    )
    ziel_hst: str = field(
        metadata={
            "name": "ZielHst",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    auf_azb: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AufAZB",
            "type": "Element",
            "namespace": "",
        },
    )
    via_hst1_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViaHst1Lang",
            "type": "Element",
            "namespace": "",
        },
    )
    via_hst2_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViaHst2Lang",
            "type": "Element",
            "namespace": "",
        },
    )
    via_hst3_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViaHst3Lang",
            "type": "Element",
            "namespace": "",
        },
    )
    via: List[ViaType] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "",
        },
    )
    fahrt_status: FahrtStatusType = field(
        metadata={
            "name": "FahrtStatus",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ankunftszeit_azbplan_or_ankunftszeit_azbprognose: List[
        XmlDateTime
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AnkunftszeitAZBPlan",
                    "type": XmlDateTime,
                    "namespace": "",
                },
                {
                    "name": "AnkunftszeitAZBPrognose",
                    "type": XmlDateTime,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        },
    )
    abfahrtszeit_azbplan_or_abfahrtszeit_azbprognose: List[
        XmlDateTime
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AbfahrtszeitAZBPlan",
                    "type": XmlDateTime,
                    "namespace": "",
                },
                {
                    "name": "AbfahrtszeitAZBPrognose",
                    "type": XmlDateTime,
                    "namespace": "",
                },
            ),
            "max_occurs": 4,
        },
    )
    abfahrtszeit_azbdisposition: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AbfahrtszeitAZBDisposition",
            "type": "Element",
            "namespace": "",
        },
    )
    fahrtspezialtext: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fahrtspezialtext",
            "type": "Element",
            "namespace": "",
        },
    )
    sprachausgabe: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sprachausgabe",
            "type": "Element",
            "namespace": "",
        },
    )
    halt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HaltID",
            "type": "Element",
            "namespace": "",
        },
    )
    haltepositions_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "HaltepositionsText",
            "type": "Element",
            "namespace": "",
        },
    )
    stauindikator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Stauindikator",
            "type": "Element",
            "namespace": "",
        },
    )
    fahrt_info: Optional[FahrtInfoType] = field(
        default=None,
        metadata={
            "name": "FahrtInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
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
