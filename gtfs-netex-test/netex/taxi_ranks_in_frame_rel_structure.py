from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .taxi_rank import TaxiRank

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRanksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "taxiRanksInFrame_RelStructure"

    taxi_rank: List[TaxiRank] = field(
        default_factory=list,
        metadata={
            "name": "TaxiRank",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
