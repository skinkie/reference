from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .purpose_of_grouping import PurposeOfGrouping

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PurposesOfGroupingInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "purposesOfGroupingInFrame_RelStructure"

    purpose_of_grouping: list[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
