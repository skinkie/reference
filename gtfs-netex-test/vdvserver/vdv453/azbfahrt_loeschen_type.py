from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype


@dataclass(kw_only=True)
class AzbfahrtLoeschenType:
    class Meta:
        name = "AZBFahrtLoeschenType"

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
    ursache: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ursache",
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
