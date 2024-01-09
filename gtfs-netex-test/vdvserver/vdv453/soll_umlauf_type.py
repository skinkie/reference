from dataclasses import dataclass, field
from typing import List, Union
from .soll_fahrt_type import SollFahrtType
from .soll_umlauf_fahrt_type import SollUmlaufFahrtType


@dataclass(kw_only=True)
class SollUmlaufType:
    umlauf_id: str = field(
        metadata={
            "name": "UmlaufID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    soll_fahrt_or_soll_umlauf_fahrt: List[
        Union[SollFahrtType, SollUmlaufFahrtType]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SollFahrt",
                    "type": SollFahrtType,
                    "namespace": "",
                },
                {
                    "name": "SollUmlaufFahrt",
                    "type": SollUmlaufFahrtType,
                    "namespace": "",
                },
            ),
        },
    )
