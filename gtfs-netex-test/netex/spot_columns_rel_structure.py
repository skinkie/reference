from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .spot_column import SpotColumn

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotColumnsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "spotColumns_RelStructure"

    spot_column: List[SpotColumn] = field(
        default_factory=list,
        metadata={
            "name": "SpotColumn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
