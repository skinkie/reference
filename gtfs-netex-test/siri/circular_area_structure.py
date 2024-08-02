from dataclasses import dataclass, field
from typing import Optional

from .location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CircularAreaStructure(LocationStructure):
    radius: Optional[int] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
