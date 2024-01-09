from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .aktive_abos_type import AktiveAbosType
from .status_type import StatusType


@dataclass(kw_only=True)
class ClientStatusAntwortType:
    status: StatusType = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    start_dienst_zst: XmlDateTime = field(
        metadata={
            "name": "StartDienstZst",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    aktive_abos: Optional[AktiveAbosType] = field(
        default=None,
        metadata={
            "name": "AktiveAbos",
            "type": "Element",
            "namespace": "",
        },
    )
