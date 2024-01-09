from dataclasses import dataclass, field
from typing import List
from .visfahrplanlage_type import VisfahrplanlageType
from .visfahrt_loeschen_type import VisfahrtLoeschenType


@dataclass(kw_only=True)
class VisnachrichtType:
    class Meta:
        name = "VISNachrichtType"

    visfahrplanlage: List[VisfahrplanlageType] = field(
        default_factory=list,
        metadata={
            "name": "VISFahrplanlage",
            "type": "Element",
            "namespace": "",
        },
    )
    visfahrt_loeschen: List[VisfahrtLoeschenType] = field(
        default_factory=list,
        metadata={
            "name": "VISFahrtLoeschen",
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
