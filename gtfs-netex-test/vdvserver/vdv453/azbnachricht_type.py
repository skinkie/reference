from dataclasses import dataclass, field
from typing import List
from .azbfahrplan_type import AzbfahrplanType
from .azbfahrplanlage_type import AzbfahrplanlageType
from .azbfahrt_loeschen_type import AzbfahrtLoeschenType
from .azblinienspezialtext_loeschen_type import (
    AzblinienspezialtextLoeschenType,
)
from .azblinienspezialtext_type import AzblinienspezialtextType


@dataclass(kw_only=True)
class AzbnachrichtType:
    class Meta:
        name = "AZBNachrichtType"

    azbfahrplan: List[AzbfahrplanType] = field(
        default_factory=list,
        metadata={
            "name": "AZBFahrplan",
            "type": "Element",
            "namespace": "",
        },
    )
    azbfahrplanlage: List[AzbfahrplanlageType] = field(
        default_factory=list,
        metadata={
            "name": "AZBFahrplanlage",
            "type": "Element",
            "namespace": "",
        },
    )
    azbfahrt_loeschen: List[AzbfahrtLoeschenType] = field(
        default_factory=list,
        metadata={
            "name": "AZBFahrtLoeschen",
            "type": "Element",
            "namespace": "",
        },
    )
    azblinienspezialtext: List[AzblinienspezialtextType] = field(
        default_factory=list,
        metadata={
            "name": "AZBLinienspezialtext",
            "type": "Element",
            "namespace": "",
        },
    )
    azblinienspezialtext_loeschen: List[
        AzblinienspezialtextLoeschenType
    ] = field(
        default_factory=list,
        metadata={
            "name": "AZBLinienspezialtextLoeschen",
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
