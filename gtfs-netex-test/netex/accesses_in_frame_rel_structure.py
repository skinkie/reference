from dataclasses import dataclass, field

from .access import Access
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessesInFrame_RelStructure"

    access: list[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
