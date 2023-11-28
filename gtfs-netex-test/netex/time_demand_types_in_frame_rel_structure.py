from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.time_demand_type import TimeDemandType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TIME DEMAND TYPE.
    """
    class Meta:
        name = "timeDemandTypesInFrame_RelStructure"

    time_demand_type: List[TimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
