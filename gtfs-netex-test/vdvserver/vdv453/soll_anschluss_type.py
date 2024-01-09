from dataclasses import dataclass, field
from typing import Optional
from .fahrt_idtype import FahrtIdtype


@dataclass(kw_only=True)
class SollAnschlussType:
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    halt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HaltID",
            "type": "Element",
            "namespace": "",
        },
    )
    umsteigewegezeit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Umsteigewegezeit",
            "type": "Element",
            "namespace": "",
        },
    )
    sitzenbleiben: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sitzenbleiben",
            "type": "Element",
            "namespace": "",
        },
    )
