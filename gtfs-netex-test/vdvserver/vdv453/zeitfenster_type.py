from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class ZeitfensterType:
    gueltig_von: XmlDateTime = field(
        metadata={
            "name": "GueltigVon",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    gueltig_bis: XmlDateTime = field(
        metadata={
            "name": "GueltigBis",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
