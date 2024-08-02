from dataclasses import dataclass, field
from typing import List, Optional

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DescriptionContentStructure:
    description_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    description_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DescriptionPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
