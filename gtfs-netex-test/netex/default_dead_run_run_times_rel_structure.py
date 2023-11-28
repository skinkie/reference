from dataclasses import dataclass, field
from typing import List
from netex.default_dead_run_run_time import DefaultDeadRunRunTime
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultDeadRunRunTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of properties of DEFAULT DEAD RUN / RUN TIME.
    """
    class Meta:
        name = "defaultDeadRunRunTimes_RelStructure"

    default_dead_run_run_time: List[DefaultDeadRunRunTime] = field(
        default_factory=list,
        metadata={
            "name": "DefaultDeadRunRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
