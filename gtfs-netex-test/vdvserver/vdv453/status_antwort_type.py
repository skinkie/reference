from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime
from .status_type import StatusType


@dataclass(kw_only=True)
class StatusAntwortType:
    status: StatusType = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    daten_bereit: bool = field(
        metadata={
            "name": "DatenBereit",
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
