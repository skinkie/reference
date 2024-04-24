from dataclasses import dataclass, field
from typing import List

from .sensor_in_entrance import SensorInEntrance
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorsInEntranceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "sensorsInEntrance_RelStructure"

    sensor_in_entrance: List[SensorInEntrance] = field(
        default_factory=list,
        metadata={
            "name": "SensorInEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
