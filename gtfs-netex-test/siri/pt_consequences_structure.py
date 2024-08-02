from dataclasses import dataclass, field
from typing import List

from .pt_consequence_structure import PtConsequenceStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PtConsequencesStructure:
    consequence: List[PtConsequenceStructure] = field(
        default_factory=list,
        metadata={
            "name": "Consequence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
