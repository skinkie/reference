from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.turnaround_time_limit_time import TurnaroundTimeLimitTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TurnaroundTimeLimitTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of properties of TURNAROUND TIME LIMIT.
    """
    class Meta:
        name = "turnaroundTimeLimitTimes_RelStructure"

    turnaround_time_limit_time: List[TurnaroundTimeLimitTime] = field(
        default_factory=list,
        metadata={
            "name": "TurnaroundTimeLimitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
