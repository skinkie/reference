from dataclasses import dataclass, field
from typing import List

from .review import Review

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReviewsRelStructure:
    class Meta:
        name = "reviews_RelStructure"

    review: List[Review] = field(
        default_factory=list,
        metadata={
            "name": "Review",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
