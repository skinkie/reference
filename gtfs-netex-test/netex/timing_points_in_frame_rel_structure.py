from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .timing_point import TimingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPointsInFrame_RelStructure"

    timing_point: list[TimingPoint] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
