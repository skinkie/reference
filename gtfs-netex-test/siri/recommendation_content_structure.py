from dataclasses import dataclass, field
from typing import List, Optional

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RecommendationContentStructure:
    recommendation_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "RecommendationText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    recommendation_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "RecommendationPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
