from dataclasses import dataclass, field
from typing import List, Union
from .ges_anschluss_type import GesAnschlussType
from .ist_fahrt_type import IstFahrtType
from .ist_umlauf_type import IstUmlaufType
from .linien_fahrplan_type import LinienFahrplanType
from .soll_umlauf_type import SollUmlaufType


@dataclass(kw_only=True)
class AusnachrichtType:
    class Meta:
        name = "AUSNachrichtType"

    choice: List[
        Union[
            LinienFahrplanType,
            SollUmlaufType,
            IstFahrtType,
            IstUmlaufType,
            GesAnschlussType,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Linienfahrplan",
                    "type": LinienFahrplanType,
                    "namespace": "",
                },
                {
                    "name": "SollUmlauf",
                    "type": SollUmlaufType,
                    "namespace": "",
                },
                {
                    "name": "IstFahrt",
                    "type": IstFahrtType,
                    "namespace": "",
                },
                {
                    "name": "IstUmlauf",
                    "type": IstUmlaufType,
                    "namespace": "",
                },
                {
                    "name": "GesAnschluss",
                    "type": GesAnschlussType,
                    "namespace": "",
                },
            ),
        },
    )
    abo_id: int = field(
        metadata={
            "name": "AboID",
            "type": "Attribute",
            "required": True,
        }
    )
