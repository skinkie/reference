from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype
from .fahrt_info_type import FahrtInfoType
from .fahrt_status_type import FahrtStatusType


@dataclass(kw_only=True)
class AsbfahrplanlageType:
    class Meta:
        name = "ASBFahrplanlageType"

    asbid: str = field(
        metadata={
            "name": "ASBID",
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
    auf_asb: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AufASB",
            "type": "Element",
            "namespace": "",
        },
    )
    ankunftszeit_asbplan: XmlDateTime = field(
        metadata={
            "name": "AnkunftszeitASBPlan",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ankunftszeit_asbprognose: XmlDateTime = field(
        metadata={
            "name": "AnkunftszeitASBPrognose",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fahrt_status: FahrtStatusType = field(
        metadata={
            "name": "FahrtStatus",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    umsteige_willige: Optional[int] = field(
        default=None,
        metadata={
            "name": "UmsteigeWillige",
            "type": "Element",
            "namespace": "",
        },
    )
    zubringer_hst_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZubringerHstLang",
            "type": "Element",
            "namespace": "",
        },
    )
    spaeteste_abbringer_info: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SpaetesteAbbringerInfo",
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
