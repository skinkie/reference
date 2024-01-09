from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .linien_filter_type import LinienFilterType
from .zeitfenster_type import ZeitfensterType


@dataclass(kw_only=True)
class AboAusrefType:
    class Meta:
        name = "AboAUSRefType"

    zeitfenster: ZeitfensterType = field(
        metadata={
            "name": "Zeitfenster",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    linienfilter: List[LinienFilterType] = field(
        default_factory=list,
        metadata={
            "name": "Linienfilter",
            "type": "Element",
            "namespace": "",
        },
    )
    umlauf_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UmlaufID",
            "type": "Element",
            "namespace": "",
        },
    )
    fahrplan_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FahrplanVersionID",
            "type": "Element",
            "namespace": "",
        },
    )
    daten_vorhanden_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DatenVorhandenBis",
            "type": "Element",
            "namespace": "",
        },
    )
    mit_ges_anschluss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MitGesAnschluss",
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
