from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .spot_row import SpotRow

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotRowsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "spotRows_RelStructure"

    spot_row: List[SpotRow] = field(
        default_factory=list,
        metadata={
            "name": "SpotRow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
