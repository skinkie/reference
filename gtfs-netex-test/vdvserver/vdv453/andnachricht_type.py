from dataclasses import dataclass, field
from typing import List
from .andmeldung_loeschen_type import AndmeldungLoeschenType
from .andmeldung_type import AndmeldungType


@dataclass(kw_only=True)
class AndnachrichtType:
    class Meta:
        name = "ANDNachrichtType"

    andmeldung: List[AndmeldungType] = field(
        default_factory=list,
        metadata={
            "name": "ANDMeldung",
            "type": "Element",
            "namespace": "",
        },
    )
    andmeldung_loeschen: List[AndmeldungLoeschenType] = field(
        default_factory=list,
        metadata={
            "name": "ANDMeldungLoeschen",
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
