from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype
from .fahrt_info_type import FahrtInfoType


@dataclass(kw_only=True)
class AzbfahrplanType:
    class Meta:
        name = "AZBFahrplanType"

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
    ankunftszeit_azbplan: XmlDateTime = field(
        metadata={
            "name": "AnkunftszeitAZBPlan",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    abfahrtszeit_azbplan: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "AbfahrtszeitAZBPlan",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
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
