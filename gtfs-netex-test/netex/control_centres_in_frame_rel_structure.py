from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControlCentresInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "controlCentresInFrame_RelStructure"

    control_centre: list[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
