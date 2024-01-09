from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .ergebnis_type import ErgebnisType


@dataclass(kw_only=True)
class BestaetigungType:
    fehlertext: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fehlertext",
            "type": "Element",
            "namespace": "",
        },
    )
    daten_gueltig_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DatenGueltigBis",
            "type": "Element",
            "namespace": "",
        },
    )
    kuerz_moeglicher_zyklus: Optional[int] = field(
        default=None,
        metadata={
            "name": "KuerzMoeglicherZyklus",
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
    ergebnis: ErgebnisType = field(
        metadata={
            "name": "Ergebnis",
            "type": "Attribute",
            "required": True,
        }
    )
    fehlernummer: str = field(
        metadata={
            "name": "Fehlernummer",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{0,10}",
        }
    )
