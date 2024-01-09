from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype
from .fahrt_info_type import FahrtInfoType
from .fahrt_status_type import FahrtStatusType


@dataclass(kw_only=True)
class VisfahrplanlageType:
    class Meta:
        name = "VISFahrplanlageType"

    visid: str = field(
        metadata={
            "name": "VISID",
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
    fahrt_status: FahrtStatusType = field(
        metadata={
            "name": "FahrtStatus",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    verspaetung: Optional[int] = field(
        default=None,
        metadata={
            "name": "Verspaetung",
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
    end_hst: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndHst",
            "type": "Element",
            "namespace": "",
        },
    )
    akt_hst: Optional[str] = field(
        default=None,
        metadata={
            "name": "AktHst",
            "type": "Element",
            "namespace": "",
        },
    )
    hst_seq_zaehler: Optional[int] = field(
        default=None,
        metadata={
            "name": "HstSeqZaehler",
            "type": "Element",
            "namespace": "",
        },
    )
    auf_hst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AufHst",
            "type": "Element",
            "namespace": "",
        },
    )
    nach_hst: Optional[str] = field(
        default=None,
        metadata={
            "name": "NachHst",
            "type": "Element",
            "namespace": "",
        },
    )
    distanz: Optional[int] = field(
        default=None,
        metadata={
            "name": "Distanz",
            "type": "Element",
            "namespace": "",
        },
    )
    geschwindigkeit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Geschwindigkeit",
            "type": "Element",
            "namespace": "",
        },
    )
    kompass_richtung: Optional[int] = field(
        default=None,
        metadata={
            "name": "KompassRichtung",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 0,
            "max_inclusive": 359,
        },
    )
    longitude: Optional[int] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "",
        },
    )
    latitude: Optional[int] = field(
        default=None,
        metadata={
            "name": "Latitude",
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
