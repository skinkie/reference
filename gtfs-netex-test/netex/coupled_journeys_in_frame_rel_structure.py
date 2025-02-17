from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .coupled_journey import CoupledJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CoupledJourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coupledJourneysInFrame_RelStructure"

    coupled_journey: list[CoupledJourney] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
