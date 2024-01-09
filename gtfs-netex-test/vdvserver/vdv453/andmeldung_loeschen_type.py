from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AndmeldungLoeschenType:
    class Meta:
        name = "ANDMeldungLoeschenType"

    meldungs_id: str = field(
        metadata={
            "name": "MeldungsID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )
