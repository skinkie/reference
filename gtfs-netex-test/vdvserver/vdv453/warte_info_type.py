from dataclasses import dataclass, field
from typing import Optional, Union
from .zurueckhaltung_bis_type import ZurueckhaltungBisType


@dataclass(kw_only=True)
class WarteInfoType:
    wartet_nicht_or_zurueckhaltung_bis: Optional[
        Union[str, ZurueckhaltungBisType]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WartetNicht",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "ZurueckhaltungBis",
                    "type": ZurueckhaltungBisType,
                    "namespace": "",
                },
            ),
        },
    )
