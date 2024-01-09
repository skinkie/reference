from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class FahrtIdextType:
    class Meta:
        name = "FahrtIDExtType"

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
    hst_seq_zaehler: int = field(
        metadata={
            "name": "HstSeqZaehler",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
