from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class TraktionsType:
    traktions_id: str = field(
        metadata={
            "name": "TraktionsID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    anzahl_fahrten: Optional[int] = field(
        default=None,
        metadata={
            "name": "AnzahlFahrten",
            "type": "Element",
            "namespace": "",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
        },
    )
