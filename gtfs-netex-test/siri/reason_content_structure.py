from dataclasses import dataclass, field
from typing import List

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ReasonContentStructure:
    reason_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
