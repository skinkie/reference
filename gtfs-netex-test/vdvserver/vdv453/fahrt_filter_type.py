from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime
from .fahrt_idtype import FahrtIdtype


@dataclass(kw_only=True)
class FahrtFilterType:
    fahrt_id: FahrtIdtype = field(
        metadata={
            "name": "FahrtID",
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
    ankunftszeit_asbplan: XmlDateTime = field(
        metadata={
            "name": "AnkunftszeitASBPlan",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vorschauzeit: int = field(
        metadata={
            "name": "Vorschauzeit",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
