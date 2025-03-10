from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .time_interval import TimeInterval
from .time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeIntervalsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timeIntervals_RelStructure"

    time_interval_ref_or_time_interval: list[Union[TimeIntervalRef, TimeInterval]] = field(
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
        },
    )
