from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class FahrtIdtype:
    class Meta:
        name = "FahrtIDType"

    fahrt_bezeichner: str = field(
        metadata={
            "name": "FahrtBezeichner",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    betriebstag: XmlDate = field(
        metadata={
            "name": "Betriebstag",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
