from dataclasses import dataclass, field
from typing import Optional

from .place_name_structure import PlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ViaNameStructure(PlaceNameStructure):
    via_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ViaPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
