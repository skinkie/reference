from dataclasses import dataclass

from .review_structure import ReviewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Review(ReviewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
