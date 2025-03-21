from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .geographical_interval import GeographicalInterval
from .geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeographicalIntervalsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "geographicalIntervals_RelStructure"

    geographical_interval_ref_or_geographical_interval: list[Union[GeographicalIntervalRef, GeographicalInterval]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalInterval",
                    "type": GeographicalInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
