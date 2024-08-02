from dataclasses import dataclass, field
from typing import List

from .administrative_area_versioned_ref_structure import AdministrativeAreaVersionedRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AdministrativeAreaRefsStructure:
    administrative_area_ref: List[AdministrativeAreaVersionedRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
