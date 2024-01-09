from dataclasses import dataclass, field
from typing import List, Union
from .ist_fahrt_type import IstFahrtType
from .ist_umlauf_fahrt_type import IstUmlaufFahrtType


@dataclass(kw_only=True)
class IstUmlaufType:
    umlauf_id: str = field(
        metadata={
            "name": "UmlaufID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ist_fahrt_or_ist_umlauf_fahrt: List[
        Union[IstFahrtType, IstUmlaufFahrtType]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "IstFahrt",
                    "type": IstFahrtType,
                    "namespace": "",
                },
                {
                    "name": "IstUmlaufFahrt",
                    "type": IstUmlaufFahrtType,
                    "namespace": "",
                },
            ),
        },
    )
