from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class FahrtStartEndeType:
    start_halt_id: str = field(
        metadata={
            "name": "StartHaltID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    startzeit: XmlDateTime = field(
        metadata={
            "name": "Startzeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    end_halt_id: str = field(
        metadata={
            "name": "EndHaltID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    endzeit: XmlDateTime = field(
        metadata={
            "name": "Endzeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
