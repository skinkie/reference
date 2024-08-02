from dataclasses import dataclass, field
from typing import List, Optional

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConsequenceContentStructure:
    consequence_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConsequenceText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    consequence_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConsequencePriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
