from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.purpose_of_grouping import PurposeOfGrouping

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposesOfGroupingInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of PURPOSE OF GROUPING.
    """
    class Meta:
        name = "purposesOfGroupingInFrame_RelStructure"

    purpose_of_grouping: List[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
