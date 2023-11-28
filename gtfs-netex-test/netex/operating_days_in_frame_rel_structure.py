from dataclasses import dataclass, field
from typing import List
from netex.alternative_texts_rel_structure import OperatingDay
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDaysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of OPERATING DAY.
    """
    class Meta:
        name = "operatingDaysInFrame_RelStructure"

    operating_day: List[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
