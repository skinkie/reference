from dataclasses import dataclass, field
from typing import Optional
from .fahrt_idglobal_type import FahrtIdglobalType


@dataclass(kw_only=True)
class AnschlussPlanType:
    zubringer: FahrtIdglobalType = field(
        metadata={
            "name": "Zubringer",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    halt_idzubringer: str = field(
        metadata={
            "name": "HaltIDZubringer",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    abbringer: FahrtIdglobalType = field(
        metadata={
            "name": "Abbringer",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    halt_idabbringer: str = field(
        metadata={
            "name": "HaltIDAbbringer",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    umsteigewegezeit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Umsteigewegezeit",
            "type": "Element",
            "namespace": "",
        },
    )
    max_auto_verzoegerung: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxAutoVerzoegerung",
            "type": "Element",
            "namespace": "",
        },
    )
    prioritaet: Optional[int] = field(
        default=None,
        metadata={
            "name": "Prioritaet",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 3,
            "total_digits": 1,
        },
    )
    anschluss_id: str = field(
        metadata={
            "name": "AnschlussID",
            "type": "Attribute",
            "required": True,
        }
    )
