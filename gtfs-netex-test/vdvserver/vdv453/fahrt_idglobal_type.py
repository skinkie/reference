from dataclasses import dataclass, field
from typing import Optional
from .fahrt_idext_type import FahrtIdextType


@dataclass(kw_only=True)
class FahrtIdglobalType:
    class Meta:
        name = "FahrtIDGlobalType"

    fahrt_idext: FahrtIdextType = field(
        metadata={
            "name": "FahrtIDExt",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    linien_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
        },
    )
    leitstellen_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LeitstellenID",
            "type": "Element",
            "namespace": "",
        },
    )
