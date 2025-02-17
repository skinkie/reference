from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice import Notice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class NoticesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticesInFrame_RelStructure"

    notice: list[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
