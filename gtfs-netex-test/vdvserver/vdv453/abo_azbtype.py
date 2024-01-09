from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AboAzbtype:
    class Meta:
        name = "AboAZBType"

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
    linien_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
        },
    )
    richtungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
        },
    )
    vorschauzeit: int = field(
        metadata={
            "name": "Vorschauzeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    max_anzahl_fahrten: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxAnzahlFahrten",
            "type": "Element",
            "namespace": "",
        },
    )
    hysterese: int = field(
        metadata={
            "name": "Hysterese",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    max_text_laenge: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxTextLaenge",
            "type": "Element",
            "namespace": "",
        },
    )
    abo_id: int = field(
        metadata={
            "name": "AboID",
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
