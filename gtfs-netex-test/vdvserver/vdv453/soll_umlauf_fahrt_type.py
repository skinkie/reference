from dataclasses import dataclass, field
from .soll_fahrt_type import SollFahrtType


@dataclass(kw_only=True)
class SollUmlaufFahrtType:
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    soll_fahrt: SollFahrtType = field(
        metadata={
            "name": "SollFahrt",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
