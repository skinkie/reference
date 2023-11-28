from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.notice import Notice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  NOTICEs.
    """
    class Meta:
        name = "noticesInFrame_RelStructure"

    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
