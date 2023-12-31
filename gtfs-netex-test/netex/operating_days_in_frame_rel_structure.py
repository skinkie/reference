from dataclasses import dataclass, field
from typing import List
from .alternative_texts_rel_structure import OperatingDay
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingDaysInFrame_RelStructure"

    operating_day: List[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
