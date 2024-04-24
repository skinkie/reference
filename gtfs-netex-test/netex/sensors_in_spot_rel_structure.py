from dataclasses import dataclass, field
from typing import List

from .sensor_in_spot import SensorInSpot
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorsInSpotRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "sensorsInSpot_RelStructure"

    sensor_in_spot: List[SensorInSpot] = field(
        default_factory=list,
        metadata={
            "name": "SensorInSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
