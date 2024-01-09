from dataclasses import dataclass, field
from typing import List
from .asbfahrplan_type import AsbfahrplanType
from .asbfahrplanlage_type import AsbfahrplanlageType
from .asbfahrt_loeschen_type import AsbfahrtLoeschenType


@dataclass(kw_only=True)
class ZubringernachrichtType:
    asbfahrplan: List[AsbfahrplanType] = field(
        default_factory=list,
        metadata={
            "name": "ASBFahrplan",
            "type": "Element",
            "namespace": "",
        },
    )
    asbfahrplanlage: List[AsbfahrplanlageType] = field(
        default_factory=list,
        metadata={
            "name": "ASBFahrplanlage",
            "type": "Element",
            "namespace": "",
        },
    )
    asbfahrt_loeschen: List[AsbfahrtLoeschenType] = field(
        default_factory=list,
        metadata={
            "name": "ASBFahrtLoeschen",
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
