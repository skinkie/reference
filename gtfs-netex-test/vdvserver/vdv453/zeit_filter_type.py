from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class ZeitFilterType:
    linien_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinienID",
            "type": "Element",
            "namespace": "",
        },
    )
    richtungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RichtungsID",
            "type": "Element",
            "namespace": "",
        },
    )
    frueheste_ankunftszeit: XmlDateTime = field(
        metadata={
            "name": "FruehesteAnkunftszeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    spaeteste_ankunftszeit: XmlDateTime = field(
        metadata={
            "name": "SpaetesteAnkunftszeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
