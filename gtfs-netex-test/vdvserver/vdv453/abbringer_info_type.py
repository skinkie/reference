from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype
from .fahrt_info_type import FahrtInfoType


@dataclass(kw_only=True)
class AbbringerInfoType:
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    hst_seq_zaehler: Optional[int] = field(
        default=None,
        metadata={
            "name": "HstSeqZaehler",
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
    abfahrtszeit_asbplan: XmlDateTime = field(
        metadata={
            "name": "AbfahrtszeitASBPlan",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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
    fahrt_info: Optional[FahrtInfoType] = field(
        default=None,
        metadata={
            "name": "FahrtInfo",
            "type": "Element",
            "namespace": "",
        },
    )
