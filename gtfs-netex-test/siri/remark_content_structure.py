from dataclasses import dataclass, field
from typing import List, Optional

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RemarkContentStructure:
    remark: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    remark_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "RemarkPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
