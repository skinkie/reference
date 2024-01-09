from dataclasses import dataclass, field
from typing import List
from .fahrt_idtype import FahrtIdtype
from .fahrt_start_ende_type import FahrtStartEndeType


@dataclass(kw_only=True)
class FahrtRefType:
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fahrt_start_ende: List[FahrtStartEndeType] = field(
        default_factory=list,
        metadata={
            "name": "FahrtStartEnde",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
