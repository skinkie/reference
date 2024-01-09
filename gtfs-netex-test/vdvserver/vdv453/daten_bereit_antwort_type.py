from dataclasses import dataclass, field
from .bestaetigung_type import BestaetigungType


@dataclass(kw_only=True)
class DatenBereitAntwortType:
    bestaetigung: BestaetigungType = field(
        metadata={
            "name": "Bestaetigung",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
