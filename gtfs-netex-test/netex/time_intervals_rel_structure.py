from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.time_interval import TimeInterval
from netex.time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeIntervalsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TIME INTERVALs.
    """
    class Meta:
        name = "timeIntervals_RelStructure"

    time_interval_ref_or_time_interval: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeInterval",
                    "type": TimeInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
