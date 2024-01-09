from dataclasses import dataclass, field
from typing import List, Union
from .abbringer_fahrt_loeschen_type import AbbringerFahrtLoeschenType
from .haltepositions_aenderung_type import HaltepositionsAenderungType
from .wartet_bis_type import WartetBisType


@dataclass(kw_only=True)
class AbbringernachrichtType:
    haltepositions_aenderung_or_wartet_bis_or_abbringer_fahrt_loeschen: List[
        Union[
            HaltepositionsAenderungType,
            WartetBisType,
            AbbringerFahrtLoeschenType,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HaltepositionsAenderung",
                    "type": HaltepositionsAenderungType,
                    "namespace": "",
                },
                {
                    "name": "WartetBis",
                    "type": WartetBisType,
                    "namespace": "",
                },
                {
                    "name": "AbbringerFahrtLoeschen",
                    "type": AbbringerFahrtLoeschenType,
                    "namespace": "",
                },
            ),
        },
    )
    abo_id: int = field(
        metadata={
            "name": "AboID",
            "type": "Attribute",
            "required": True,
        }
    )
