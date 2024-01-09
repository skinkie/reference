from dataclasses import dataclass, field
from .ist_fahrt_type import IstFahrtType


@dataclass(kw_only=True)
class IstUmlaufFahrtType:
    linien_id: str = field(
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ist_fahrt: IstFahrtType = field(
        metadata={
            "name": "IstFahrt",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
