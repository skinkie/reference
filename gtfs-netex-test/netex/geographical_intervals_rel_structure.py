from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.geographical_interval import GeographicalInterval
from netex.geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL INTERVALs.
    """
    class Meta:
        name = "geographicalIntervals_RelStructure"

    geographical_interval_ref_or_geographical_interval: List[object] = field(
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
        }
    )
